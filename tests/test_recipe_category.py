import unittest

from app.models.recipeCategory import RecipeCategory

class TestRecipeCategory(unittest.TestCase):
    def setUp(self):
        self.recipe_category = RecipeCategory('Stews')

    def test_add_recipe_to_recipe_category(self):
        self.recipe_category.add_recipe_to_recipe_category('Chicken Stew')
        self.assertEqual(self.recipe_category.view_recipes(), ['Chicken Stew'])

    def test_delete_recipe_from_recipe_category(self):
        self.recipe_category.add_recipe_to_recipe_category('Chicken Stew')
        self.recipe_category.add_recipe_to_recipe_category('Beef Stew')
        self.recipe_category.delete_recipe_from_recipe_category('Chicken Stew')
        self.assertEqual(self.recipe_category.view_recipes(), ['Beef Stew'])

    def test_view_recipe_categories(self):
        self.recipe_category.add_recipe_to_recipe_category('Chicken Stew')
        self.recipe_category.add_recipe_to_recipe_category('Beef Stew')
        self.recipe_category.add_recipe_to_recipe_category('Ham Stew')
        self.assertEqual(self.recipe_category.view_recipes(), ['Chicken Stew', 'Beef Stew', 'Ham Stew'])
