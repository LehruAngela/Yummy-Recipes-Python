class RecipeCategory(object):
    """Class with methods for a recipe category"""

    def __init__(self, name, recipes=None):
        self.name = name
        self.recipes = recipes or [] #list of recipes contained in the recipes

    def add_recipe_to_recipe_category(self, recipe):
        """add a recipe to a recipe category"""
        self.recipes.append(recipe)

    def delete_recipe(self, recipe):
        """delete a recipe from recipe category"""
        if len(self.recipes) > 0 and recipe in self.recipes:
            self.recipes.remove(recipe)
        else:
            raise ValueError

    def view_recipes(self):
        """View the entire list of recipes in a recipe category"""
        return self.recipes
