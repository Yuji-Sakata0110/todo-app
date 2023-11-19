from flask import Blueprint, jsonify

todos = Blueprint("todos", __name__)


@todos.route("/api/todos")
def get_todos() -> list[dict]:
    response: list[dict] = [
        {"id": 1, "title": "sample", "description": "sample", "completed": False},
        {"id": 2, "title": "sample2", "description": "sample2", "completed": True},
    ]
    return jsonify(response)
