import unittest

from app.models.user import User
from app.models.recipeApp import RecipeApp


class TestRecipeApp(unittest.TestCase):
    """class to test valid user registration and login."""
    def setUp(self):
        self.app = RecipeApp()
        self.user = User('Angela', 'angelalehru@gmail.com', '1234')

    def test_login_with_correct_email_and_password(self):
        """user to login with correct email and password"""
        self.app.signup(self.user)
        self.assertTrue(self.app.login('angelalehru@gmail.com','1234'))

    def test_login_with_incorrect_email(self):
        """user cannot login with incorrect email."""
        self.app.signup(self.user)
        self.assertFalse(self.app.login('angelajamimah@gmail.com', '1234'))

    def test_login_with_incorrect_password(self):
        """user cannot login with incorrect password"""
        self.app.signup(self.user)
        self.assertFalse(self.app.login('angelalehru@gmail.com', '5678'))

    def test_login_with_incorrect_email_and_incorrect_password(self):
        """user cannot login with both incorrect email and incorrect password"""
        self.app.signup(self.user)
        self.assertFalse(self.app.login('angelajamimah@gmail.com', '5678'))
