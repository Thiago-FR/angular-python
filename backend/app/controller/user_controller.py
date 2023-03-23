from flask import jsonify, request
import json
import pymongo


class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def find_all_users(self):
        result = self.user_service.find_all_users()

        return json.dumps(result, default=str), 200

    def create_users(self):
        try:
            name = request.json["name"]
            email = request.json["email"]
            phone = request.json["phone"]

            user = {"name": name, "email": email, "phone": phone}

            self.user_service.create_users(user)

            return jsonify({"message": True}), 201

        except pymongo.errors.DuplicateKeyError:
            return jsonify({"message": "Id já existe"}), 401

        except (KeyError, ValueError):
            return jsonify({"message": "Todos os campos devem ser preenchidos"}), 401

    def update_user(self, id):
        try:
            name = request.json["name"]
            email = request.json["email"]
            phone = request.json["phone"]

            user = {"name": name, "email": email, "phone": phone}

            self.user_service.update_user(id, user)

            return jsonify({"message": "Update True"}), 200
        except KeyError:
            return jsonify({"message": "Todos os campos devem ser preenchidos"}), 401
        except ValueError as error:
            message, code = str(error).split("|")

            return jsonify({"message": message}), code

    def delete_user(self, user_id):
        try:
            self.user_service.delete_user(user_id)

            return jsonify({"message": "Delete True"}), 200
        except ValueError as error:
            message, code = str(error).split("|")

            return jsonify({"message": message}), code
