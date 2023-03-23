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

            user = {"name": name}

            self.user_service.create_users(user)

            return jsonify({"message": True}), 201
        except pymongo.errors.DuplicateKeyError:
            return jsonify({"message": "Id já existe"}), 401
        except (KeyError, ValueError):
            return jsonify({
                "message": "Todos os campos devem ser preenchidos"
            }), 401
