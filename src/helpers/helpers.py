from src.model.product import Product
from src.dtos.product_dto import ProductDTO
from typing import Any, List

def product_to_model(product: List[Any]) -> Product:
    return Product(
        nome_produto=product[1],
        empresa=product[2],
        saldo_min=product[3],
        cod_sku=product[4],
        consumo_mensal=product[5],
        ativo=product[6],
        data_cadastro=product[7],
        data_atualizacao=product[8],
    )