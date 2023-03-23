class UserModel:
    def __init__(self, db):
        self.db = db

    def find_all_users(self):
        result = list(self.db.users.find())

        return result

    def find_one_users(self, user_id):
        result = self.db.users.find_one({"_id": user_id})

        return result

    def create_users(self, user):
        self.db.users.insert_one(user)
