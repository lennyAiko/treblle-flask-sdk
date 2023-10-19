from flask import Flask, request, jsonify
import json

app = Flask(__name__)
# Treblle(app)

## helpers

def read_file():
    f = open('data/db.json', 'r')
    db = f.read()
    db = db.replace('\'', '"')
    db = json.loads(db)
    f.close()
    return db

def save_file(db):
    f = open('data/db.json', 'w')
    f.write(str(json.dumps(db)))
    f.close()

## callbacks

@app.before_request
def before_request_callback():
    global db
    db = read_file()

@app.after_request
def after_request_callback(response):
    save_file(db)
    return response

## routes

@app.route('/', methods=['GET'])
def articles():
    return jsonify(db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)