from flask import Flask
from routes.ProverbsRoutes import routes_proverbs

app = Flask(__name__)

app.register_blueprint(routes_proverbs, url_prefix= "/api/proverbs")
if __name__ == "__main__":
    app.run(debug=True)