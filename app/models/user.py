class User(object):
    """class for user attributes and methods"""
    def __init__(self, username, email, password, recipe_categories=None):
        self.username = username
        self.email = email
        self.password = password
        self.recipe_categories = recipe_categories or []

    def create_recipe_category(self, recipe_category):
        """Method to add a recipe category"""
        self.recipe_categories.append(recipe_category)

    def delete_recipe_category(self, recipe_category):
        """Method to delete a recipe category"""
        self.recipe_categories.remove(recipe_category)

    def view_recipe_categories(self):
        """Method to view recipe categories created"""
        return self.recipe_categories
