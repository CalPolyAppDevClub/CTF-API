from flask import Flask, jsonify, request, g
import sqlite3, sys

app = Flask(__name__)

DATABASE = 'game.db'


@app.route("/")
def helloRoot():
    return "hello"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/post/<int:post_id>")
def hello(post_id):
    id = '%d' % post_id
    return jsonify({
        "here is the id": id
    })

@app.route('/api/games', methods=['GET'])
def get_games():
    # Connect to the database
    cur = get_db().cursor()
    # Query the database for games, (game is the table we are querying)
    query = "select * from game"
    db_data = cur.execute(query).fetchall()
    response_data = []
    for row in db_data:
        response_data.append(row[1])
        print( " " +  row[1]  +" ", file=sys.stdout)
    # Return the data as JSON
    return jsonify({"data" :response_data})


@app.route('/api/test', methods=['POST'])
def get_home():
    req_body = request.get_json()
    
    
    print(request.get_json(), file=sys.stdout)
    return jsonify({"Hello": "it works"})


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


if __name__ == '__main__':
    app.run(debug=True)