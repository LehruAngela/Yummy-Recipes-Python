class User(object):
    """class for user attributes and methods"""
    def __init__(self, username, email, password, recipe_categories=None, public_recipes=None):
        self.username = username
        self.email = email
        self.password = password
        self.recipe_categories = recipe_categories or []
        self.public_dict = []

    def create_recipe_category(self, recipe_category):
        """Method to add a recipe category"""
        self.recipe_categories.append(recipe_category)

    def delete_recipe_category(self, recipe_category):
        """Method to delete a recipe category"""
        self.recipe_categories.remove(recipe_category)

    def view_recipe_categories(self):
        """Method to view recipe categories created"""
        return self.recipe_categories

    def create_public_recipe(self, public_recipe):
        """Method to add a public recipe"""
        self.public_dict.append(public_recipe)

    def delete_public_recipe(self, public_recipe):
        """Method to delete a public recipe"""
        self.public_dict.remove(public_recipe)

    def view_public_recipes(self):
        """Method to view public recipes created"""
        return self.public_dict
