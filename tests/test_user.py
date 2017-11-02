import unittest

from app.models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('Angela', 'angelalehru@gmail.com', '1234')

    def test_create_shopping_list(self):
        self.user.create_recipe_category('bags')
        self.assertEqual(self.user.view_recipe_categories(), ['bags'])

    def test_delete_shopping_list(self):
        self.user.create_recipe_category('cakes')
        self.user.create_recipe_category('stews')
        self.user.delete_recipe_category('cakes')
        self.assertEqual(self.user.view_recipe_categories(), ['stews'] )

    def test_view_shopping_lists(self):
        self.user.create_recipe_category('cakes')
        self.user.create_recipe_category('stews')
        self.user.create_recipe_category('salads')
        self.assertEqual(self.user.view_recipe_categories(), ['cakes', 'stews', 'salads'])
