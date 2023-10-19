from flask import Flask, request, jsonify
import json

app = Flask(__name__)
# Treblle(app)

## helpers

def read_file(file_name):
    f = open(f'data/{file_name}.json', 'r')
    db = f.read()
    db = db.replace('\'', '"')
    db = json.loads(db)
    f.close()
    return db

def save_file(db, file_name):
    f = open(f'data/{file_name}.json', 'w')
    f.write(str(json.dumps(db)))
    f.close()

## callbacks

@app.before_request
def before_request_callback():
    global articles_db, users_db
    articles_db = read_file()
    users_db = read_file()

@app.after_request
def after_request_callback(response):
    save_file(articles_db)
    save_file(users_db)
    return response

## routes

@app.route('/', methods=['GET'])
def articles():
    return jsonify(articles_db)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)