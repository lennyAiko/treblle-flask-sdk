from flask import Flask, request, jsonify
import uuid

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)
from treblle_flask import Treblle

app = Flask(__name__)
Treblle(app)

app.config["JWT_SECRET_KEY"] = "treblle-flask-sdk"
jwt = JWTManager(app)

## DB
articles_db = []
users_db = []


## callbacks
@app.after_request
def after_request_callback(response):
    # response.headers['Content-Encoding'] = 'gzip'
    response.headers["Content-Type"] = "application/json"
    response.headers["X-Frame-Options"] = "deny"
    response.headers["Accept"] = "application/json"
    response.headers["Allow"] = "GET, POST, PATCH, DELETE"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


## routes
@app.route("/signup", methods=["POST"])
def create_user():
    payload = request.get_json()
    user_id = uuid.uuid4()
    for i in users_db:
        if payload["username"] == i["username"]:
            return {"message": "Username already exists"}, 409
    payload["id"] = str(user_id)
    users_db.append(payload)
    show = payload.copy()
    show["password"] = "*" * len(show["password"])
    return show, 201


@app.route("/signin", methods=["POST"])
def sign_user():
    payload = request.get_json()
    for i in users_db:
        if payload["username"] == i["username"]:
            if payload["password"] == i["password"]:
                access_token = create_access_token(identity=payload["username"])
                return {"token": access_token}, 201
    return {"message": "Password incorrect"}, 401


@app.route("/", methods=["GET", "POST"])
@jwt_required()
def articles():
    current_user = get_jwt_identity()
    if request.method == "GET":
        user_articles = []
        for i in articles_db:
            if current_user == i["author"]:
                user_articles.append(i)
        return user_articles, 200
    else:
        payload = request.get_json()
        for i in articles_db:
            if payload["title"] == i["title"]:
                return {"message": "oops! already exists"}, 400
        payload["id"] = str(uuid.uuid4())
        payload["author"] = current_user
        articles_db.append(payload)
        return payload, 201


@app.route("/<art_id>", methods=["PATCH", "DELETE", "GET"])
@jwt_required()
def single_article(art_id):
    current_user = get_jwt_identity()
    if request.method == "GET":
        for i in articles_db:
            if str(art_id) == str(i["id"]):
                if current_user == i["author"]:
                    return i, 200, {"Allow": "GET"}
        return {"message": "not found"}, 404
    elif request.method == "PATCH":
        payload = request.get_json()
        for i in articles_db:
            if str(art_id) == str(i["id"]):
                if current_user == i["author"]:
                    i["title"] = payload["title"]
                    i["body"] = payload["body"]
                    return i, 200
        return {"message": "not found"}, 404
    else:
        for i in articles_db:
            if str(art_id) == str(i["id"]):
                if current_user == i["author"]:
                    articles_db.remove(i)
                    return {"message": "Successful"}, 200
        return {"message": "not found"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
