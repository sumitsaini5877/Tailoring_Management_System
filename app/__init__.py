from flask import Flask 
from .routes.auth import auth_bp
from .extensions import db , migrate , login_manager

def create_app():
    # Application factory: creates and configures the Flask app instance.
    app = Flask(__name__)

    app.config.from_object("app.config.Config")  # Load configuration from the Config class.    

    # Register the authentication blueprint routes.
    app.register_blueprint(auth_bp)

    # Initialize extensions with the app instance.
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from app import models  # Import models to register them with SQLAlchemy

    return app
