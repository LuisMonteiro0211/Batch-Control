from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class ProductDTO:
    name: str
    minimun_balance: int
    product_firm: str
    product_code_chb: int
    consumption_monthly: float

    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None