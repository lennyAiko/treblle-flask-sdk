from flask import Flask, request, jsonify
import json

app = Flask(__name__)
# Treblle(app)

## DB
articles_db = []
users_db = []

## helpers


## callbacks


## routes

@app.route('/', methods=['GET'])
def articles():
    return jsonify(articles_db)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)