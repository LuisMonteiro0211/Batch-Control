from dataclasses import dataclass, field

from src.dtos.product_dto import ProductDTO
from src.dtos.batch_dto import BatchDTO

@dataclass
class AppContext:
    products: list[ProductDTO] = field(default_factory=list)
    batches: list[BatchDTO] = field(default_factory=list)