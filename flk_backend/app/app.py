from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models.models import db
from controllers.todos import todos
from controllers.auth import auth


app = Flask(__name__)
# BluePrintを利用し、用途に合ったルーティングに通信を回す。
app.register_blueprint(todos, url_prefix="/api")
app.register_blueprint(auth, url_prefix="/api/auth")


# database定義に必要な設定
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite3"

# Set up Flask-JWT-Extended
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)


# マイグレーション。もう少しわかりやすい用途にしたい。
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello() -> str:
    return jsonify("Hello, World!")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
