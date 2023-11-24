import hashlib
from models.models import User


def hash_password(password: str) -> str:
    encoded_password: bytes = password.encode("utf-8")
    hashed_object = hashlib.sha256(encoded_password)
    hashed_password: str = hashed_object.hexdigest()
    return hashed_password


def check_email(email: str) -> bool:
    email = User.query.filter_by(email=email).first()

    if email:
        return True
    else:
        return False


# def authenticate(username, password):
#     user = User.get(username, None)
#     if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
#         return user
# def identity(payload):
#     user_id = payload["identity"]
#     return userid_table.get(user_id, None)
