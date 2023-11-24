from typing import Any
from flask import Blueprint, jsonify, request, Response, make_response
from flask_jwt_extended import create_access_token
from controllers.utils.auth_funcs import hash_password, check_email
from controllers.constants.error_messages import (
    BAD_REQUEST_ERROR,
    NotFound_ERROR,
)
from models.models import User

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["POST"])
def signup() -> dict[str, Any]:
    """
    body str username
    body str password
    return dict "access_token", "refresh_token"
    """

    email = request.json.get("email", None)

    if check_email(email):
        password = request.json.get("password", None)
        hashed_password: str = hash_password(password)

        # save new user

        # login

        # add reccord of user_id in database
        response: dict = {
            "message": "succeed to signup your account.",
            "access_token": "",
            "refresh_token": "",
        }
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


# test api
@auth.route("/test/generate/token", methods=["POST"])
def get_token() -> Response | dict:
    username = request.json.get("username", None)
    if username is None:
        response: dict[str, str] = {
            "error": BAD_REQUEST_ERROR,
            "message": "Missing username parameter",
        }
        return jsonify(response), 400

    access_token: str = create_access_token(identity=username)
    message: dict[str, str] = {"message": "succeed to set cookie."}

    response: Response = make_response(jsonify(message))
    response.set_cookie("access_token", value=access_token, httponly=True, secure=True)

    return response, 200


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
