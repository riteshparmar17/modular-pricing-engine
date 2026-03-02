from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    User login
    ---
    tags:
      - Authentication
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
              password:
                type: string
    responses:
      200:
        description: JWT access token
      401:
        description: Invalid credentials
    """
    username = request.json.get("username")
    password = request.json.get("password")

    # Simple demo authentication
    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad credentials"}), 401