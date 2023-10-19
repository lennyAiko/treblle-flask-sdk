from flask import Flask, request, jsonify
import uuid

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
# Treblle(app)

app.config["JWT_SECRET_KEY"] = "treblle-flask-sdk" 
jwt = JWTManager(app)

## DB
articles_db = []
users_db = []

## helpers


## callbacks


## routes

@app.route('/', methods=['GET'])
def articles():
    return jsonify(articles_db)

@app.route('/sign_up', methods=['POST'])
def create_user():
    payload = request.get_json()
    user_id = uuid.uuid4()
    for i in users_db:
        if payload['username'] == i['username']:
            return {"message": "Username already exists"}, 409
    payload['id'] = str(user_id)
    users_db.append(payload)
    show = payload.copy()
    show['password'] = '*' * len(show['password'])
    return jsonify(show), 201

@app.route('/login', methods=['POST'])
def login_user():
    payload = request.get_json()

    for i in users_db:
        if payload["username"] == i['username']:
            if payload["password"] != i['password']:
                return {"message": "Password incorrect"}, 401
            else:
                access_token = create_access_token(identity=payload['username'])
                return {"token": access_token}, 201
        else:
            return {"message": "Invalid username"}, 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)