from dataclasses import dataclass
from typing import Optional

@dataclass
class Pricing:
    product_id: str
    base_price: float
    discount: Optional[float] = 0.0

    def final_price(self) -> float:
        return round(self.base_price - (self.base_price * self.discount), 2)
    