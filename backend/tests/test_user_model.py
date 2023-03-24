from app.model.user_model import UserModel
from .mock import mock_db

user_model = UserModel(mock_db)


def test_model_find_all_users():
    result = user_model.find_all_users()
    assert result == mock_db.find()


def test_model_find_one_users():
    id = "507f191e810c19729de860ea"
    result = user_model.find_one_users(id)
    assert result == mock_db.find_one(id)


def test_model_create_users():
    result = user_model.create_users({})
    assert not result


def test_model_update_users():
    id = "507f191e810c19729de860ea"
    result = user_model.update_user(id, {})
    assert result


def test_model_delete_users():
    id = "507f191e810c19729de860ea"
    result = user_model.delete_user(id)
    assert result
