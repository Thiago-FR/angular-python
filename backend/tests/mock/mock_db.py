def find():
    mongo = [
        {
            "_id": 1,
            "name": "Thiago Rose",
            "email": "thiago@test.com.br",
            "phone": "4199998888"
        }
      ]

    return mongo


def find_one(id):
    mongo = {
            "_id": 1,
            "name": "Thiago Rose",
            "email": "thiago@test.com.br",
            "phone": "4199998888"
        }

    return mongo


def insert_one(obj):
    return True


def find_one_and_update(id, user):
    return True


def find_one_and_delete(id):
    return True
