import pytest
from app.services.pricing_service import PricingService
from app.models.pricing_model import Pricing


class MockRepo:
    def __init__(self):
        self.storage = {}

    def get_by_product_id(self, product_id):
        return self.storage.get(product_id)

    def save(self, pricing):
        self.storage[pricing.product_id] = pricing


def test_create_price():
    repo = MockRepo()
    service = PricingService(repo)

    data = {
        "product_id": "A1",
        "base_price": 100,
        "discount": 0.1
    }

    result = service.create_or_update_price(data)
    print("RESULT:", result)

    assert result["message"] == "Pricing saved successfully"