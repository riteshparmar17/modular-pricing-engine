from pymongo.collection import Collection
from app.models.pricing_model import Pricing
from typing import Optional

class PricingRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def get_by_product_id(self, product_id: str) -> Optional[Pricing]:
        data = self.collection.find_one({"product_id": product_id})

        if not data:
            return None
        
        return Pricing(
            product_id=data["product_id"],
            base_price=data["base_price"],
            discount=data.get("discount", 0.0)
        )
    
    def save(self, pricing: Pricing) -> None:
        self.collection.update_one(
            {"product_id": pricing.product_id},
            {
                "$set":{
                    "base_price": pricing.base_price,
                    "discount": pricing.discount
                }
            },
            upsert=True
        )
