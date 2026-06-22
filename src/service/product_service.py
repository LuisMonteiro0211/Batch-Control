from typing import Any, List, Tuple
from src.dtos.product_dto import ProductDTO
from src.exceptions import DuplicateSkuError, ProductHasBalanceError
from src.model.product import Product
from src.repository.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def create_product(self, product_dto: ProductDTO) -> int:
        # Verificar se o código SKU já existe
        if self._product_repository.sku_exists(product_dto.product_code_chb):
            raise DuplicateSkuError(product_dto.product_code_chb)

        # Criação do objeto Product
        product = Product(
            nome_produto=product_dto.name,
            empresa=product_dto.product_firm,
            saldo_min=product_dto.minimun_balance,
            cod_sku=product_dto.product_code_chb,
            consumo_mensal=product_dto.consumption_monthly,
        )

        return self._product_repository.create(entity=product)

    def delete_product(self, id_produto: int) -> None:
        
        saldo_produto = None #Futura chamada do repo de lote

        if saldo_produto > 0:
            raise ProductHasBalanceError(f'Não é possível deletar o produto com ID {id_produto} pois ele possui saldo ativo.')
        else:
            self._product_repository.delete(id=id_produto)

    def update_product(self, id_produto: int, list_to_update: List[Tuple[str, Any]]) -> None:
        #Sanitização dos dados
        #Busca do produto (Estado anterior)
        #Comparação entre os dois estados
        #Atualização do produto
        #Retorno do produto atualizado

        product_old = self._product_repository.get_by_id(id=id_produto)
        
        pass