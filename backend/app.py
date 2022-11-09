import firebase_admin
from firebase_admin import credentials
from flask import Flask, jsonify, request


from models.user import User, UserSchema

app = Flask(__name__)
cred = credentials.Certificate("../firebase-service-account-key.json")
firebase_admin.initialize_app(cred)


@app.route("/")
def home():

    return "home"


@app.route("/users", methods=["POST"])
def add_user():
    UserSchema().load(request.get_json())
    return "", 404
