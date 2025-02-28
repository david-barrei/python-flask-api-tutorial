from flask import Flask, jsonify
from flask import request


app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    request_body = jsonify(todos)
    return request_body



@app.route('/todos-read', methods=['GET'])
def hello_world1():
    json_text = jsonify(todos)
    return json_text


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

