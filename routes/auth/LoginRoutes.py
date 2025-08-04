from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import create_access_token
from controllers.AuthController import AuthController


routes_auth = Blueprint("routes_auth", __name__)

auth_controller = AuthController()

@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or data is None:
        return jsonify({"error": "Bad request."}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password."}), 400

    login_req = auth_controller.login(username, password)
    if login_req:
        access_token = create_access_token(identity=username)
        return jsonify({"status": "success",
                        "access_token": access_token,
                        "expires_in": int(current_app.config["JWT_ACCESS_TOKEN_EXPIRES"].total_seconds())}), 200
    return jsonify({"status": "failed"}), 401
