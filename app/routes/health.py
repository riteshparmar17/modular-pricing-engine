from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__, url_prefix="/api")

@health_bp.route("/health", methods=["GET"])
def health():
    """
    Basic health check endpoint.
    Used for monitoring and load balancer checks.
    """
    return jsonify({
        "status": "healthy",
        "service": "module-pricing-enginge"
    }), 200