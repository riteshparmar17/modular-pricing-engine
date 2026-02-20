from app.repositories.pricing_repository import PricingRepository
from app.models.pricing_model import Pricing

class PricingService:
    def __init__(self, repository: PricingRepository):
        self.repository = repository
    
    def get_final_price(self, product_id: str) -> dict:
        pricing = self.repository.get_by_product_id(product_id)

        if not pricing:
            return {"error": "Product not found"}

        return {
            "product_id": pricing.product_id,
            "base_price": pricing.base_price,
            "discount": pricing.discount,
            "final_price": pricing.final_price()
        }
    
    def create_or_update_price(self, data: dict) -> dict:
        pricing = Pricing(
            product_id=data["product_id"],
            base_price=float(data["base_price"]),
            discount=float(data.get("discount", 0.0))
        )

        self.repository.save(pricing)

        return {"message": "Pricing saved successfully"}