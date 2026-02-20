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

@pricing_bp.route("/pricing/<product_id>", methods=["GET"])
def get_price(product_id):
    service = get_service()
    result = service.get_final_price(product_id)
    return jsonify(result)

@pricing_bp.route("/pricing", methods=["POST"])
def create_price():
    service = get_service()
    result = service.create_or_update_price(request.json)
    return jsonify(result)