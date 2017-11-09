from flask import Flask, render_template, redirect, url_for, session, request
from app import app
from app.models.user import User
from app.models.recipeCategory import RecipeCategory
from app.models.recipe import Recipe
from app.models.recipeApp import RecipeApp

import os

app.secret_key=os.urandom(24)

users = RecipeApp()


@app.route('/')
def index():
    if 'email' in session:
        email = session['email']
        username = users[email].username
        return redirect(url_for('view_recipe_categories', user_x = username))
    return redirect(url_for('signup'))


@app.route('/signup', methods=['POST', 'GET'] )
def signup():
    if request.method == 'POST':
        # read form data and save it
        username = request.form['username'];
        email = request.form['email'];
        password = request.form['password'];

        user = User(username, email, password)
        if users.signup(user):
            return redirect(url_for('login'))
    return render_template('signup.html');


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if users.login(email, password):
            session['email'] = email
            username = users.users_dict.get(email,False).username
            return redirect(url_for('view_recipe_categories', user_x=username))
    return render_template('login.html');


@app.route('/<user_x>/recipeCategories')
def view_recipe_categories(user_x):
    """Method to view recipe categories"""
    if 'email' in session:
        user = users.users_dict[session['email']]
        recipe_categories = user.view_recipe_categories()
        return render_template('viewCategories.html', recipe_categories = recipe_categories,
                               username=user.username, category_index=len(recipe_categories), title = 'Your Categories')
    return render_template('login.html')


@app.route('/<user_x>/create', methods=['POST', 'GET'])
def create_recipe_category(user_x):
    """Method to add a recipe category"""
    if 'email' not in session:
        return render_template('login.html')
    user = users.users_dict[session['email']]
    if request.method == 'POST':
        name = request.form['category_name']
        recipe_category = RecipeCategory(name)
        user.create_recipe_category(recipe_category)
        return redirect(url_for('add_recipe_to_category', category_index=len(user.recipe_categories)-1))
    return render_template('createCategory.html', username=user.username, title = 'Add Category')


@app.route('/recipeCategory/<category_index>', methods=['POST', 'GET'])
def add_recipe_to_category(category_index):
    """Method to add recipes to recipe category"""
    if 'email' not in session:
        return render_template('login.html')
    user = users.users_dict[session['email']]
    category_name=user.recipe_categories[int(category_index)].name
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        directions = request.form['directions']
        user.recipe_categories[int(category_index)].add_recipe_to_recipe_category(Recipe(name, ingredients, directions))
        return redirect(url_for('view_recipes',category_index=category_index))
    return render_template('addRecipesToCategory.html', username=user.username, title = 'Add recipes', category_name = category_name)


@app.route('/recipeCategory/<category_index>/recipes')
def view_recipes(category_index):
    """Method to view recipes in recipe category"""
    if 'email' not in session:
        return render_template('login.html')
    user = users.users_dict[session['email']]
    category_name=user.recipe_categories[int(category_index)].name
    recipes = user.recipe_categories[int(category_index)].view_recipes()
    return render_template('viewRecipes.html', recipes=recipes,
                           recipeCategory=user.recipe_categories[int(category_index)].name,
                           recipe_len=len(recipes), category_index=category_index,
                           username=user.username, title = 'Recipes')


@app.route('/recipeCategory/<category_id>/update', methods=['POST', 'GET'])
def update_recipe_category(category_id):
    """Method for user to edit recipe category"""
    if 'email' not in session:
        return render_template('login.html')
    user = users.users_dict[session['email']]
    if request.method == 'POST':
        name = request.form['category_name']
        user.recipe_categories[int(category_id)].name = name
        return redirect(url_for('view_recipe_categories',
                                user_x=user.username))
    return render_template('updateCategory.html',
                           username=user.username,
                           category_name=user.recipe_categories[int(category_id)].name, title = 'Edit')


@app.route('/<category_id>/delete')
def delete_recipe_category(category_id):
    """Method to delete recipe category"""
    if 'email' not in session:
        return render_template('login.html')
    try:
        user = users.users_dict[session['email']]
        recipe_category = user.recipe_categories[int(category_id)]
        user.delete_recipe_category(recipe_category)
        return redirect(url_for('view_recipe_categories', user_x=user.username))
    except ValueError:
        return redirect(url_for('view_recipe_categories', user_x=user.username))


@app.route('/recipeCategory/<category_index>/recipe/<recipe_id>/update', methods=['POST', 'GET'])
def update_recipes(category_index, recipe_id):
    """Method for user to add items to shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users.users_dict[session['email']]
    recipe_category = user.recipe_categories[int(category_index)]
    recipe = recipe_category.recipes[int(recipe_id)]
    if request.method == 'POST':
        new_name = request.form['name']
        new_ingredients = request.form['ingredients']
        new_directions = request.form['directions']

        recipe.name = new_name
        recipe.quantity = new_ingredients
        recipe.quantity = new_ingredients

        return redirect(url_for('view_recipes', category_index=category_index))
    return render_template('updateRecipe.html',username=user.username, name=recipe.name,
                            ingredients=recipe.ingredients, directions=recipe.directions,title = 'Edit Recipe')


@app.route('/<category_index>/<recipe_id>/delete')
def delete_recipe_from_category(category_index, recipe_id):
    """Method to delete recipe from recipe category"""
    if 'email' not in session:
        return render_template('login.html')
    try:
        user = users.users_dict[session['email']]
        recipe_category = user.recipe_categories[int(category_index)]
        recipe = recipe_category.recipes[int(recipe_id)]
        recipe_category.delete_recipe(recipe)
        return redirect(url_for('view_recipes', category_index=category_index))
    except ValueError:
        return redirect(url_for('view_recipes', category_index=category_index))


@app.route('/<user_x>/publicRecipes', methods=['POST', 'GET'])
def public_recipes(user_x):
    """Method to view public recipes"""
    if 'email' not in session:
        return render_template('login.html')
    user = users.users_dict[session['email']]
    recipes = user.view_public_recipes()
    return render_template('viewPublicRecipes.html', recipes=recipes, public_len=len(user.public_dict), username=user.username, title = 'Public Recipes')


@app.route('/<user_x>/create_public_recipe', methods=['POST', 'GET'])
def create_public_recipes(user_x):
    """Method to create public recipes"""
    if 'email' not in session:
        return render_template('login.html')
    user = users.users_dict[session['email']]
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        directions = request.form['directions']
        user.create_public_recipe(Recipe(name, ingredients, directions))
        return redirect(url_for('public_recipes', user_x=user.username))
    return render_template('createPublicRecipe.html', username=user.username, title = 'Add Recipe')


@app.route('/logout')
def logout():
    """Remove email from session"""
    session.pop('email', None)
    return redirect(url_for('index'))
