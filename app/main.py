from flask import Flask, jsonify, request

app = Flask(__name__)

# in memory data store

todos = []


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the To-Do List API!"}), 200


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "Task field is required"}), 400

    todo = {
        'id': len(todos) + 1,
        'task': data['task'],
        'done': False
    }
    todos.append(todo)
    return jsonify(todo), 201

