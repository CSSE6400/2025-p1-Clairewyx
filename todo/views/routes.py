from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api/v1')

# 假设是存储在内存中的数据
todos = [
    {
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }
]

@api.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo:
        return jsonify(todo), 200
    return jsonify({"error": "Todo not found"}), 404

@api.route('/todos', methods=['POST'])
def post_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(new_todo), 201

@api.route('/todos/<int:todo_id>', methods=['PUT'])
def put_todo(todo_id):
    updated_todo = request.get_json()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[i] = updated_todo
            return jsonify(updated_todo), 200
    return jsonify({"error": "Todo not found"}), 404

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200
