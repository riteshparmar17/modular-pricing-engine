from flask import Flask
from app.config import Config
from app.routes.health import health_bp

def create_app(config_class=Config):
    """
    Application factory function.
    Creates and configures the Flask app instance.
    """

    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Register blueprints
    app.register_blueprint(health_bp)

    return app