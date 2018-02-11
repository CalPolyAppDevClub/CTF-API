from flask import Flask, jsonify, request
import sys, os

app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
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