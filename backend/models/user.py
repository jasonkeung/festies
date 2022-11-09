from firebase_admin import firestore
from marshmallow import fields, post_load, Schema


class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserSchema(Schema):
    name = fields.Str()
    age = fields.Number()

    @post_load
    def make_user(self, data, **kwargs):  # may need to add **kwargs
        users_collection = firestore.client().collection("users")
        # create a unique UserId here
        res = users_collection.document("userid1").set(
            {
                "name": data["name"],
                "age": data["age"],
            }
        )

        return User(**data)
