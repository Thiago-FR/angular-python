from flask import Blueprint

from ..controller.user_controller import UserController
from ..services.user_service import UserService
from ..model.user_model import UserModel
from ..config.database import db


user = Blueprint("user", __name__)

LIST_URL = "/api/v1/user"

user_model = UserModel(db)
user_service = UserService(user_model)
user_controller = UserController(user_service)


@user.route(LIST_URL, methods=["GET"])
def get_all_user():
    return user_controller.find_all_users()


@user.route(LIST_URL, methods=["POST"])
def create_user():
    return user_controller.create_users()
