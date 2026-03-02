from flask import Flask
from flasgger import Swagger
from app.config import Config
from app.routes.health import health_bp
from app.api.pricing_routes import pricing_bp
from app.errors import register_error_handlers
from app.extensions import mongo
from flask_jwt_extended import JWTManager

def create_app(config_class=Config):
    """
    Application factory function.
    Creates and configures the Flask app instance.
    """

    app = Flask(__name__)
    app.config.from_object(config_class)
    
    #JWT secret
    jwt = JWTManager(app)

    mongo.init_app(app)

    swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Modular Pricing Engine API",
        "description": "Pricing service with JWT authentication",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}

    Swagger(app, template=swagger_template)

    # Register error handlers
    register_error_handlers(app)

    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(pricing_bp)

    return app