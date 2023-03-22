def find_all_users(db):
    result = list(db.find())

    return result


def find_one_users(db, user_id):
    result = db.find_one({"_id": user_id})

    return result


def create_users(db, user):
    db.insert_one(user)


def update_users(db, user_id, user):
    db.find_one_and_update({"_id": user_id}, {"$set": user})


def delete_users(db, user_id):
    db.find_one_and_delete({"_id": user_id})
