class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def find_all_users(self):
        result = self.user_model.find_all_users()

        return result

    def create_users(self, user):
        return self.user_model.create_users(user)

    def update_user(self, user_id, user):
        # if description == '' or user == '' or status == '':
        #     raise ValueError("Todos os campos devem ser preenchidos|400")

        get_user = self.user_model.find_one_users(user_id)

        if get_user is None:
            raise ValueError("Id não encontrado|404")

        # format_user = {
        #         "_id": 1,
        #         "description": description,
        #         "user": user,
        #         "status": status,
        #     }

        self.user_model.update_user(user_id, user)

    def delete_user(self, user_id):
        get_user = self.user_model.find_one_users(user_id)

        if get_user is None:
            raise ValueError("Id não encontrado|404")

        self.user_model.delete_user(user_id)
