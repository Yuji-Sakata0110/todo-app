from flask_jwt_extended import create_access_token


def generate_token(username: str) -> str:
    access_token: str = create_access_token(identity=username)
    return access_token
    # username = request.json.get("username", None)
    # if username is None:
    #     response: dict[str, str] = {
    #         "error": BAD_REQUEST_ERROR,
    #         "message": "Missing username parameter",
    #     }
    #     return jsonify(response), 400
