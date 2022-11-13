import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

from models.event import Event
from models.group import Group
from models.user import User

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = "/api"
API_URL = "/static/swagger.yaml"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Festies"}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

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


@app.route("/events")
def get_events():
    snapshot = db.collection("events").stream()
    # TODO: catch the type errors thrown by Event and handle
    return [vars(Event(doc.to_dict())) for doc in snapshot]


@app.route("/events", methods=["POST"])
def set_event():
    events_collection = firestore.client().collection("events")
    new_event = Event(request.get_json())
    events_collection.document(new_event.names).set(vars(new_event))
    return "", 200


if __name__ == "__main__":
    app.run(debug=True)
