from typing import List
from flask import Blueprint, jsonify, request
from models.models import db, Todo

todos = Blueprint("todos", __name__)


@todos.route("/todos", methods=["GET"])
def get_todos() -> jsonify:
    todos: List = Todo.query.all()
    response: list[dict[str, str | bool]] = [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed,
        }
        for todo in todos
    ]
    return jsonify(response), 200


@todos.route("/todos", methods=["POST"])
def post_todos() -> jsonify:
    try:
        body: dict = request.get_json()
        # body analyzer
        new_todo = Todo(
            title=body["title"],
            description=body["description"],
            completed=body["completed"],
            user_id=body["user_id"],
        )
        db.session.add(new_todo)
        db.session.commit()
        response: dict = {"message": "success to add this new todo"}
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
