from flask import Blueprint, current_app, jsonify
from app.extensions import mongo

health_bp = Blueprint("health", __name__, url_prefix="/api")

@health_bp.route("/health", methods=["GET"])
def health_check():

    try:
        mongo.cx.admin.command('ping')
        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200
    except Exception:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected"
        }), 500