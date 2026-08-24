"""
Módulo de serviço de produtos.

Encapsula a lógica de negócio de produtos, delegando persistência
ao ProductRepository e convertendo dados para DTOs.
"""

from dataclasses import replace
from typing import List
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

    def update_product(self, original_product_dto: ProductDTO, edited_product_dto: ProductDTO) -> None:


        pass

    def get_product_lower_minimum_balance(self) -> List[ProductCardDTO]:
        """
        Retorna produtos com saldo abaixo do mínimo, com nível de estoque calculado.

        Returns:
            Lista de ProductCardDTO prontos para exibição na tabela do dashboard.
        """
        products_lower_minimum_balance = self._product_repository.get_product_lower_minimum_balance()
        return [
            replace(
                dict_to_product_card_dto(product=product),
                stock_level=sort_level(
                    current_stock=int(product["estoque_atual"]),
                    min_stock=int(product["saldo_min"]),
                ),
            )
            for product in products_lower_minimum_balance
        ]

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
