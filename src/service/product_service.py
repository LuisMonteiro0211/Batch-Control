"""
Módulo de serviço de produtos.

Encapsula a lógica de negócio de produtos, delegando persistência
ao ProductRepository e convertendo dados para DTOs.
"""

from typing import Any, List, Tuple
from src.dtos.product_dto import ProductDTO, ProductCardDTO
from src.exceptions import DuplicateSkuError, ProductHasBalanceError
from src.helpers.helpers import dict_to_product_card_dto, dict_to_product_dto
from src.model.product import Product
from src.model.stock_level import sort_level
from src.repository.product_repository import ProductRepository


class ProductService:
    """
    Serviço de produtos com operações CRUD e consultas de dashboard.

    Args:
        product_repository: Repositório responsável pelo acesso ao banco.
    """

    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def create_product(self, product_dto: ProductDTO) -> int:
        """
        Cria um novo produto após validar unicidade do código SKU.

        Args:
            product_dto: Dados do produto a ser criado.

        Returns:
            ID do produto criado no banco.

        Raises:
            DuplicateSkuError: Se o código SKU já existir.
        """
        if self._product_repository.sku_exists(product_dto.product_code_chb):
            raise DuplicateSkuError(product_dto.product_code_chb)

        product = Product(
            nome_produto=product_dto.name,
            empresa=product_dto.product_firm,
            saldo_min=product_dto.minimun_balance,
            cod_sku=product_dto.product_code_chb,
            consumo_mensal=product_dto.consumption_monthly,
        )

        return self._product_repository.create(entity=product)

    def delete_product(self, id_produto: int) -> None:
        """
        Remove um produto do banco, desde que não possua saldo ativo.

        Args:
            id_produto: ID do produto a ser removido.

        Raises:
            ProductHasBalanceError: Se o produto possuir saldo em lotes.
        """
        saldo_produto = None  # Futura chamada do repo de lote

        if saldo_produto > 0:
            raise ProductHasBalanceError(
                f'Não é possível deletar o produto com ID {id_produto} pois ele possui saldo ativo.'
            )
        else:
            self._product_repository.delete(id=id_produto)

    def update_product(self, id_produto: int, list_to_update: List[Tuple[str, Any]]) -> None:
        """
        Atualiza campos de um produto existente.

        Args:
            id_produto: ID do produto a ser atualizado.
            list_to_update: Lista de tuplas (coluna, novo_valor) para atualização.
        """
        product_old = self._product_repository.get_by_id(id=id_produto)

        pass

    def get_product_lower_minimum_balance(self) -> List[ProductCardDTO]:
        """
        Retorna produtos com saldo abaixo do mínimo, com nível de estoque calculado.

        Returns:
            Lista de ProductCardDTO prontos para exibição na tabela do dashboard.
        """
        products_lower_minimum_balance = self._product_repository.get_product_lower_minimum_balance()
        list_product_card_dtos = [
            dict_to_product_card_dto(product=product)
            for product in products_lower_minimum_balance
        ]

        for product in list_product_card_dtos:
            product.stock_level = sort_level(
                current_stock=product.current_balance,
                min_stock=product.minimun_balance,
            )

        return list_product_card_dtos

    def get_product_by_id(self, id_produto: int) -> ProductDTO:
        """
        Busca um produto pelo ID e converte para DTO.

        Args:
            id_produto: ID do produto no banco.

        Returns:
            ProductDTO com os dados completos do produto.
        """
        product = self._product_repository.get_by_id(id=id_produto)
        return dict_to_product_dto(product=product)
