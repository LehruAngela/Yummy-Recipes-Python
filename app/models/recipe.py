class Recipe(object):
    """Class for the recipes in a recipe category"""
    def __init__(self, name, ingredients, directions):
        self.name = name
        self.ingredients = ingredients
        self.directions = directions
