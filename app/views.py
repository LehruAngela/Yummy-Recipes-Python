from flask import Flask, render_template, redirect, url_for, session, request
from app import app
from models.user import User
from models.recipeCategory import RecipeCategory
from models.recipe import Recipe

import os

app.secret_key=os.urandom(24)

users = {}

@app.route('/')
def index():
    if 'email' in session:
        email = session['email']
        username = users[email].username
        return redirect(url_for('viewRecipeCategories', loggedin_user = username))
    return redirect(url_for('signup'))

@app.route('/signup', methods=['POST', 'GET'] )
def signup():
    if request.method == 'POST':
        # read form data and save it
        username = request.form['username'];
        email = request.form['email'];
        password = request.form['password'];

        if email in users.keys():
            return redirect(url_for('signup'), error_msg="User already exists")
        else:
            user = User(username, email, password)
            users[user.email] = user
            return redirect(url_for('login'))
    return render_template('signup.html');

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        verify = users.get(email,False)
        if email == verify.email:
            if password == verify.password:
                session['email'] = email
                username = verify.username
                return redirect(url_for('viewRecipeCategories', loggedin_user=username))
    return render_template('login.html');


@app.route('/<loggedin_user>/shoppinglists')
def viewRecipeCategories(loggedin_user):
    """Method to view user's shopping list"""
    if 'email' in session:
        user = users[session['email']]
        recipe_categories = user.view_recipe_categories()
        return render_template('viewCategories.html',
                               recipe_categories = recipe_categories,
                               username=user.username, num=len(recipe_categories), title = 'Your Categories')
    return render_template('login.html')


@app.route('/<loggedin_user>/create', methods=['POST', 'GET'])
def createRecipeCategory(loggedin_user):
    """Method for user to create shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    if request.method == 'POST':
        name = request.form['category_name']
        recipe_category = RecipeCategory(name)
        user.create_recipe_category(recipe_category)
        return redirect(url_for('addRecipesToCategory',
                                num=len(user.recipe_categories)-1))
    return render_template('createCategory.html', username=user.username, title = 'Add Category')

@app.route('/recipeCategory/<num>', methods=['POST', 'GET'])
def addRecipesToCategory(num):
    """Method for user to add items to shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    category_name=user.recipe_categories[int(num)].name
    if request.method == 'POST':
        name = request.form['recipe_name']
        ingredients = request.form['ingredients']
        directions = request.form['directions']
        user.recipe_categories[int(num)].add_recipe_to_recipe_category(Recipe(name, ingredients, directions))
        return redirect(url_for('viewRecipes',num=num))
    return render_template('addRecipesToCategory.html', username=user.username, title = 'Add recipes', category_name = category_name)


@app.route('/recipeCategory/<num>/recipes')
def viewRecipes(num):
    """Method to view items in shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    category_name=user.recipe_categories[int(num)].name
    recipes = user.recipe_categories[int(num)].view_recipes()
    return render_template('viewRecipes.html', recipes=recipes,
                           category_name=category_name,
                           recipe_num=len(recipes), category_index=num,
                           username=user.username, title = 'Recipes')


@app.route('/logout')
def logout():
    """ remove the username from the session if it is there """
    session.pop('email', None)
    return redirect(url_for('index'))
