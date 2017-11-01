import unittest

from app.models.recipeApp import RecipeApp
from app.models.user import User

class TestRecipeApp(unittest.TestCase):
    """class to test valid user registration and login."""
    def setup(self):
        self.app = RecipeApp()
        self.user = User('Angela', 'angelalehru@gmail.com', '1234')

    def test_signup(self):
        self.assertTrue(self.app.signup(User('Angela', 'angelalehru@gmail.com', '1234')))

    def test_login_with_correct_email_and_password(self):
        """user to login with correct email and password"""
        self.app.signup(self.user)
        self.assertTrue(self.app.login('angelalehru@gmail.com','1234'))

    def test_login_with_incorrect_email(self):
        """user cannot login with incorrect email."""
        self.assertFalse(self.app.login('angelajamimah@gmail.com', '1234'))

    def test_login_with_incorrect_password(self):
        """user cannot login with incorrect password"""
        self.assertFalse(self.app.login('angelalehru@gmail.com', '5678'))

    def test_login_with_incorrect_email_and_incorrect_password(self):
        """user cannot login with both incorrect email and incorrect password"""
        self.assertFalse(self.app.login('angelajamimah@gmail.com', '5678'))

"""
    def test_invalid_email_type_at_login(self):
        self.user = self.app.login('cecilia@gmail.com', '123456')
        new_user = self.app.login('cecilia.com', '123456')
        self.assertEqual(new_user, self.user, msg='Input is not an email')

    def test_for_empty_password_at_login(self):
        self.user = self.app.login('cecilia@gmail.com', '123456')
        new_user = self.app.login('cecilia@gmail.com', ' ')
        self.assertEqual(new_user, self.user, msg='Password is empty')

    def test_for_invalid_password_at_login(self):
        self.user1 = self.app.login('cecilia@gmail.com', '123456')
        new_user = self.app.login('cecilia@gmail.com', 'pass ')
        self.assertEqual(new_user, self.user1, msg='The password is invalid')

    def test_if_user_registering_already_exists(self):
        self.user = self.app.register(self.user)
        self.user1 = User('CeciliaCaroline', 'cecilia@gmail.com', '123456')
        new_user = self.app.register(self.user1)
        self.assertNotEqual(new_user, self.user, msg='This user already exists')

    def test_if_user_logging_is_not_registered(self):
        self.assertFalse(self.app.login('cecilia@gmail.com', '123456'))

"""
