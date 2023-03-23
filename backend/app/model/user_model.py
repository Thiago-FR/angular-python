class UserModel:
    def __init__(self, db):
        self.db = db

    def find_all_users(self):
        result = list(self.db.find())

        return result

    def find_one_users(self, user_id):
        result = self.db.find_one({"_id": user_id})

        return result

    def create_users(self, user):
        self.db.insert_one(user)
