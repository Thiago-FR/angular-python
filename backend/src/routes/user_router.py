from flask import Blueprint
from ..controller import user_controller
from ..services import user_service
from ..model import user_model
from ..config.database import mongo as db


user = Blueprint("user", __name__)

LIST_URL = "/api/v1/list"


@user.route(LIST_URL, methods=["GET"])
def get_all_user():
    return user_controller.find_all_users(db, user_model, user_service)


@user.route(LIST_URL, methods=["POST"])
def create_user():
    return user_controller.create_users(db, user_model, user_service)