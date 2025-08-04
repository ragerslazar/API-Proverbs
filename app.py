import os
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.ProverbsRoutes import routes_proverbs
from routes.auth.LoginRoutes import routes_auth
from datetime import timedelta

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=10800)

jwt = JWTManager(app)

@app.route("/")
def home():
    return ""

app.register_blueprint(routes_proverbs, url_prefix= "/api/v1/proverbs")
app.register_blueprint(routes_auth, url_prefix="/api/v1/auth")
if __name__ == "__main__":
    app.run(debug=True)