class Result:
    def __init__(self, inserted_id):
        self.inserted_id = inserted_id


def find():
    mongo = [
        {
            "_id": 1,
            "name": "Thiago Rose",
            "email": "thiago@test.com.br",
            "phone": "4199998888",
        }
    ]

    return mongo


def find_one(id):
    mongo = {
        "_id": 1,
        "name": "Thiago Rose",
        "email": "thiago@test.com.br",
        "phone": "4199998888",
    }

    return mongo


def insert_one(obj):
    return Result(obj['id'])


def find_one_and_update(id, user):
    return True


def find_one_and_delete(id):
    return True
