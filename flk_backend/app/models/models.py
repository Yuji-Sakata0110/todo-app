from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__: str = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    user_id_fk = db.relationship("Todo", back_populates="user_id_fk")

    def __init__(self, user_id, username, is_active) -> None:
        self.user_id = user_id
        self.username = username
        self.is_active = is_active

    def __str__(self) -> str:
        return f"user_id={self.user_id},username={self.username}"


class Todo(db.Model):
    __tablename__: str = "todo"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000))
    completed = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    user_id_fk = db.relationship("User", back_populates="user_id_fk")

    def __init__(self, title, description, completed, user_id) -> None:
        self.title = title
        self.description = description
        self.completed = completed
        self.user_id = user_id

    def __str__(self) -> str:
        return f"title={self.title}, description={self.description}, \
            completed={self.completed}, user_id={self.user_id}"
