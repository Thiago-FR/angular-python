class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def find_all_users(self):
        result = self.user_model.find_all_users()

        return result

    def create_users(self, user):
        self.user_model.create_users(user)
