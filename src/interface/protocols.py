from typing import Optional, Protocol

from src.dtos.product_dto import ProductDTO


class SaveEditProductProtocol(Protocol):
    def __call__(self) -> None: ...

class DeleteProductProtocol(Protocol):
    def __call__(self, product_id: int) -> None: ...

