"""
Exportações do pacote repository.

Os imports ficam em __getattr__ de propósito. Importar um submódulo
(por exemplo types_repository) executa este arquivo antes. Se
ProductRepository fosse importado aqui no topo, o helper — que precisa
desses tipos — voltaria a ser carregado antes de terminar de inicializar.
"""

from typing import Any

__all__ = ["ProductRepository", "FullProductData", "ProductCardDict"]


def __getattr__(name: str) -> Any:
    if name == "ProductRepository":
        from .product_repository import ProductRepository

        return ProductRepository

    if name == "FullProductData":
        from .types_repository import FullProductData

        return FullProductData

    if name == "ProductCardDict":
        from .types_repository import ProductCardDict

        return ProductCardDict

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
