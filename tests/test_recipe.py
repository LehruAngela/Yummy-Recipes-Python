import unittest

from app.models import Recipe

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.recipe= Recipe('Chicken Stew', ['chicken', 'olive oil', 'pasta'], 'Fry chicken in olive oil and mix with pasta')
