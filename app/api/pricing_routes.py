from flask import Blueprint, jsonify, request
from flask_pymongo import PyMongo
from app.repositories.pricing_repository import PricingRepository
from app.services.pricing_service import PricingService

pricing_bp = Blueprint("pricing", __name__)

mongo = PyMongo()

@pricing_bp.record_once
def on_load(state):
    app = state.app
    mongo.init_app(app)

def get_service():
    repository = PricingRepository(mongo.db.pricing)
    return PricingService(repository)

@pricing_bp.route("/price/<product_id>", methods=["GET"])
def get_price(product_id):
    service = get_service()
    result = service.get_final_price(product_id)
    return jsonify(result)

@pricing_bp.route("/price", methods=["POST"])
def create_price():
    """
    Create pricing entry
    ---
    tags:
      - Pricing
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              product_id:
                type: string
              base_price:
                type: number
              discount:
                type: number
    responses:
      200:
        description: Pricing saved successfully
      400:
        description: Validation error
    """    
    service = get_service()
    result = service.create_or_update_price(request.json)
    return jsonify(result)