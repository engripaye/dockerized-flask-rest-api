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


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = True
            return jsonify(todo), 200
    return jsonify({"error": "To-Do not found"}), 404


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({"message": "To-Do deleted"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
