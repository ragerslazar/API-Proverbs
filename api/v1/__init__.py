from .routes.ProverbsRoutes import routes_proverbs
from .routes.auth.LoginRoutes import routes_auth

def register_blueprints(app):
    app.register_blueprint(routes_proverbs, url_prefix="/api/v1/proverbs")
    app.register_blueprint(routes_auth, url_prefix="/api/v1/auth")
