class RecipeApp(object):
    def __init__(self, users_dict=None):
        self.users_dict = users_dict or {}

    def signup(self, user):
        self.users_dict[user.email] = user

    def login(self, email, password):
        """method to login in registered users"""
        if email in self.users_dict.keys():
            verify = self.users_dict.get(email,False)
            if email == verify.email and password == verify.password:
                return True
            else:
                return False
