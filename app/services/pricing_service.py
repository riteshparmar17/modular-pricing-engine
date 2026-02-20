from app.repositories.pricing_repository import PricingRepository
from app.models.pricing_model import Pricing
from app.schemas.pricing_schema import PricingCreateSchema
from pydantic import ValidationError
import logging

logger = logging.getLogger(__name__)

class PricingService:
    def __init__(self, repository: PricingRepository):
        self.repository = repository
    
    def get_final_price(self, product_id: str) -> dict:
        pricing = self.repository.get_by_product_id(product_id)

        if not pricing:
            logger.warning(f"Product with ID {product_id} not found.")
            return {"error": "Product not found"}

        return {
            "product_id": pricing.product_id,
            "base_price": pricing.base_price,
            "discount": pricing.discount,
            "final_price": pricing.final_price()
        }
    
    def create_or_update_price(self, data: dict) -> dict:
        try:
            validated = PricingCreateSchema(**data)
        except ValidationError as e:
            return {"error": e.errors()}

        pricing = Pricing(
            product_id=validated.product_id,
            base_price=validated.base_price,
            discount=validated.discount
        )

        self.repository.save(pricing)
        logger.info(f"Saving pricing for product {validated.product_id}")
        return {"message": "Pricing saved successfully"}