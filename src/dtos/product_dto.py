from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.model.stock_level import StockLevel

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


@dataclass()
class ProductCardDTO:
    product_id: int
    product_code_chb: int
    product_name: str
    product_firm: str
    minimun_balance: int
    current_balance: int
    status: int
    stock_level: Optional[StockLevel] = None
