class RecipeApp(object):
    def __init__(self):
        self.users_dict = {}

    def signup(self, user):
        """method to signup users"""
        if user.email in self.users_dict.keys():
            return False
        else:
            self.users_dict[user.email] = user
            return True

    def login(self, email, password):
        """method to login in registered users"""
        if email in self.users_dict.keys():
            verify = self.users_dict.get(email,False)
            if email == verify.email and password == verify.password:
                return True
            else:
                return False
