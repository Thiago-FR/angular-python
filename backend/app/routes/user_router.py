from flask import Blueprint

from controller.user_controller import UserController
from services.user_service import UserService
from model.user_model import UserModel
from config.database import db


user = Blueprint("user", __name__)

URL = "/api/v1/user"

user_model = UserModel(db.users)
user_service = UserService(user_model)
user_controller = UserController(user_service)


@user.route(URL, methods=["GET"])
def get_all_user():
    return user_controller.find_all_users()


@user.route(URL, methods=["POST"])
def create_user():
    return user_controller.create_users()


@user.route(f"{URL}/<id>", methods=["PUT"])
def update_user(id):
    return user_controller.update_user(id)


@user.route(f"{URL}/<id>", methods=["DELETE"])
def delete_user(id):
    return user_controller.delete_user(id)
