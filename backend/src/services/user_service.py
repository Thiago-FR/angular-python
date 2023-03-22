def find_all_users(db, user_model):
    result = user_model.find_all_users(db)

    return result


def create_users(db, user_model, user):
    user_model.create_users(db, user)


def update_users(db, user_model, user):
    user_model.update_users(db, user)


def delete_users(db, user_model, user_id):
    user_model.delete_users(db, user_id)
