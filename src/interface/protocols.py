from typing import List, Optional, Protocol

from src.dtos.product_dto import ProductCardDTO, ProductDTO


class SaveEditProductProtocol(Protocol):
    def __call__(self) -> None: ...

class DeleteProductProtocol(Protocol):
    def __call__(self, product_id: int) -> None: ...

class SearchProductByNameProtocol(Protocol):
    def __call__(self, name_product: str) -> Optional[List[ProductCardDTO]]: ...