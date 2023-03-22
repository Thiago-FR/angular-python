from flask import jsonify, request
import pymongo


def find_all_users(db, user_model, user_service):
    result = user_service.find_all_users(db, user_model)

    return jsonify(result), 200


def create_users(db, user_model, user_service):
    try:
        name = request.json["name"]

        user = {"name": name}

        user_service.create_users(db, user_model, user)

        return jsonify({"message": True}), 201
    except pymongo.errors.DuplicateKeyError:
        return jsonify({"message": "Id já existe"}), 401
    except (KeyError, ValueError):
        return jsonify({
            "message": "Todos os campos devem ser preenchidos"
            }), 401


# def update_users(db, user_model, user_service):
#     user_service.update_users(db, user_model, user)


# def delete_users(db, user_model, user_service):
#     user_service.delete_users(db, user_model, user_id)
