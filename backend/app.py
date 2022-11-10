import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, jsonify, request

from models.group import Group
from models.user import User

app = Flask(__name__)

cred = credentials.Certificate("../firebase-service-account-key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route("/")
def home():
    return "home"


@app.route("/users")
def get_users():
    snapshot = db.collection("users").stream()
    # TODO: catch the type errors thrown by User and handle
    return [vars(User(doc.to_dict())) for doc in snapshot]


@app.route("/users", methods=["POST"])
def set_user():
    users_collection = firestore.client().collection("users")
    new_user = User(request.get_json())
    users_collection.document(new_user.name).set(vars(new_user))

    return "", 200


@app.route("/groups")
def get_groups():
    snapshot = db.collection("groups").stream()
    # TODO: catch the type errors thrown by Group and handle
    return [vars(Group(doc.to_dict())) for doc in snapshot]


@app.route("/groups", methods=["POST"])
def set_group():
    groups_collection = firestore.client().collection("groups")
    new_group = Group(request.get_json())
    groups_collection.document(new_group.names).set(vars(new_group))
    return "", 200


if __name__ == "__main__":
    app.run(debug=True)
