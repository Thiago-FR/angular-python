from bson.objectid import ObjectId


class UserModel:
    def __init__(self, db):
        self.db = db

    def find_all_users(self):
        result = list(self.db.find())

        return result

    def find_one_users(self, user_id):
        result = self.db.find_one({"_id": ObjectId(user_id)})

        return result

    def create_users(self, user):
        self.db.insert_one(user)

    def update_user(self, user_id, user):
        self.db.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": user})

        return True

    def delete_user(self, user_id):
        self.db.find_one_and_delete({"_id": ObjectId(user_id)})

        return True
