from typing import Any
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from controllers.constants.error_messages import (
    BAD_REQUEST_ERROR,
    NotFound_ERROR,
)
from models.models import User

auth = Blueprint("auth", __name__)


# def authenticate(username, password):
#     user = username_table.get(username, None)
#     if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
#         return user


# def identity(payload):
#     user_id = payload["identity"]
#     return userid_table.get(user_id, None)


@auth.route("/signup", methods=["POST"])
def signup() -> dict[str, Any]:
    """
    body str username
    body str password
    return dict "access_token", "refresh_token"
    """
    users: list = User.query.all()
    # add reccord of user_id in database
    response: dict = {"message": "success", "users": users}
    return jsonify(response), 200


@auth.route("/login", methods=["POST"])
def login() -> dict[str, str]:
    """
    body str username
    body str password
    return dict "access_token", "refresh_token"
    """
    # check username, password in database and generate jwt token
    response: dict = {"message": "success"}
    return jsonify(response), 200


@auth.route("/logout", methods=["POST"])
def logout() -> dict[str, str]:
    """
    return dict[str, str] "message"
    """
    # delete reccord of user_id from database
    access_token: str | None = request.cookies.get("access_token")
    if access_token is None:
        response: dict[str, str] = {
            "error": BAD_REQUEST_ERROR,
            "message": "JWTToken is invalid.",
        }
        return jsonify(response), 400

    response: dict = {"message": "success"}
    return jsonify(response), 200


@auth.route("/token", methods=["POST"])
def get_token() -> dict[str, str]:
    username = request.json.get("username", None)
    if username is None:
        response: dict[str, str] = {
            "error": BAD_REQUEST_ERROR,
            "message": "Missing username parameter",
        }
        return jsonify(response), 400

    access_token: str = create_access_token(identity=username)

    response: dict[str, str] = {"msg": "Token set as cookie"}
    response.set_cookie("access_token", value=access_token, httponly=True, secure=True)

    return jsonify(response), 200


# test api
@auth.route("/test/token", methods=["GET"])
def test_token() -> dict:
    # Set the token as a cookie in the response
    access_token_cookie: str | None = request.cookies.get("access_token")

    if access_token_cookie:
        response: dict[str, str] = {"access_token": access_token_cookie}
        return jsonify(response), 200
    else:
        response: dict[str, str] = {
            "error": NotFound_ERROR,
            "message": "Access token cookie not found",
        }
        return jsonify(response), 404
