from pydantic import BaseModel, Field, validator

class PricingCreateSchema(BaseModel):
    product_id: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    discount: float = Field(default=0.0, ge=0, le=1)

    @validator('product_id')
    def product_id_not_blank(cls, v):
        if not v.strip():
            raise ValueError('Product ID cannot be blank')
        return v