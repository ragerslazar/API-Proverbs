from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from api.v1 import register_blueprints

from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt = JWTManager(app)

    @app.route("/")
    def home():
        return jsonify({"message": "index"}), 200

    register_blueprints(app)
    return app
