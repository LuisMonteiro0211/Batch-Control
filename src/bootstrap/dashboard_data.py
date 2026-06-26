from dataclasses import dataclass, field
from typing import List

from src.dtos.product_dto import ProductCardDTO
from src.dtos.batch_dto import BatchDTO

@dataclass
class DashboardData:
    low_stock_products: List[ProductCardDTO] = field(default_factory=list)  
    expiring_batches: List[BatchDTO] = field(default_factory=list)