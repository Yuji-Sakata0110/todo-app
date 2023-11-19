from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    __tablename__: str = "todo"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000))
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, completed) -> None:
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        return f"title={self.title},description={self.description},completed={self.completed}"
