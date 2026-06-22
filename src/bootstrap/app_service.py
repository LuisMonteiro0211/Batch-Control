from dataclasses import dataclass
from src.service.product_service import ProductService
from typing import Optional

@dataclass
class AppServices:
    product: Optional[ProductService] = None