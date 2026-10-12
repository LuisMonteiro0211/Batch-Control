"""
Módulo que representa o repositório de produtos.

Uso recomendado:
>>> from product_repository import ProductRepository

>>> product_repository = ProductRepository("database.db")

>>> product_repository.create(Product(nome_produto="Produto 1", empresa="Empresa 1", saldo_min=100, cod_sku=123456, consumo_mensal=1000))

>>> product_repository.get_all()

>>> product_repository.get_by_id(1)

>>> product_repository.get_by_cod_sku(123456)

>>> product_repository.get_by_nome_produto("Produto 1")

>>> product_repository.update(1, [("nome_produto", "Produto 2")])

>>> product_repository.delete(1)
"""

from sqlite3 import DatabaseError, IntegrityError
from typing import Any, List, final, Optional, Tuple

from data.connection_db import get_connection
from src.exceptions import (
    DatabaseOperationError,
    DuplicateSkuError,
    ProductNotFoundError,
    NoChangesError,
)
from src.helpers.helpers import row_to_full_product_data, row_to_product_card_dict
from src.interface.entity import Entity
from src.model.product import Product
from src.repository.types_repository import FullProductData, ProductCardDict

@final
class ProductRepository (Entity):
    """
    Classe que representa o repositório de produtos.

    Args:
        database_name: Nome do banco de dados.

    Returns:
        None
    """
    def __init__(self, database_name: str) -> None:
        self._database_name = database_name

    def create(self, entity: Product) -> Optional[int]:
        """
        Cria um novo produto no banco de dados.

        Args:
            entity: Produto a ser criado.

        Returns:
            ID do produto criado ou None se o produto não foi criado.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "INSERT INTO produtos (nome_produto, empresa, saldo_min, cod_sku, consumo_mensal, ativo) VALUES (?, ?, ?, ?, ?, ?)"
                values = (entity.nome_produto, entity.empresa, entity.saldo_min, entity.cod_sku, entity.consumo_mensal, 1 if entity.ativo else 0)

                cursor.execute(query, values)
                return cursor.lastrowid if cursor.lastrowid is not None else None

        except IntegrityError as e:
            raise DuplicateSkuError(entity.cod_sku) from e # Erro personalizado para código SKU duplicado
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao criar produto: {e}") from e # Erro personalizado para erro de banco de dados

    def update(self, id: int, list_to_update: List[Tuple[str, Any]]) -> Optional[int]:
        """
        Atualiza um produto no banco de dados.

        Args:
            id: ID do produto a ser atualizado.
            list_to_update: Lista de tuplas contendo o nome do campo e o valor a ser atualizado (ex: [("nome_produto", "Novo nome"), ("empresa", "Nova empresa")]).

        Returns:
            Optional[int]: quantidade de linhas afetadas.
        """

        if not list_to_update:
            raise NoChangesError("Não há alterações para atualizar.")

        try:
            with get_connection(self._database_name) as cursor:
                for field_name, value in list_to_update:
                    query = f"UPDATE produtos SET {field_name} = ? WHERE id_produto = ?"
                    values = (value, id)
                    cursor.execute(query, values)

                    return cursor.rowcount

        except IntegrityError as e:
            raise DuplicateSkuError(value) from e # Erro personalizado para código SKU duplicado

        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao atualizar produto: {e}") from e # Erro personalizado para erro de banco de dados

    def delete(self, id: int) -> Optional[int]:
        """
        Deleta um produto no banco de dados.

        Args:
            id: ID do produto a ser deletado.

        Returns:
            Optional[int]: quantidade de linhas afetadas.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "DELETE FROM produtos WHERE id_produto = ?"
                values = (id,)
                cursor.execute(query, values)

                return cursor.rowcount

        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao deletar produto: {e}") from e # Erro personalizado para erro de banco de dados

    def get_all(self) -> List[FullProductData]:
        """
        Obtém todos os produtos do banco de dados.

        Args:
            None

        Returns:
            List[FullProductData]: Lista de produtos como objetos FullProductData.
        """

        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM products_information"
                cursor.execute(query)
                products = cursor.fetchall()

                if not products:
                    raise ProductNotFoundError("Não há produtos cadastrados.")

                return [row_to_full_product_data(cursor, product) for product in products]
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter todos os produtos: {e}") from e # Erro personalizado para erro de banco de dados


    def get_by_cod_sku(self, cod_sku: int) -> Optional[FullProductData]:
        """
        Obtém um produto pelo código SKU.

        Args:
            cod_sku: Código SKU do produto a ser obtido.

        Returns:
            Optional[FullProductData]: Produto encontrado como objeto FullProductData ou None se não houver produto correspondente.
        """

        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM products_information WHERE cod_sku = ?"
                values = (cod_sku,)

                cursor.execute(query, values)
                product = cursor.fetchone()

                if product is None:
                    raise ProductNotFoundError(f"Produto com código SKU {cod_sku} não encontrado.")

                return row_to_full_product_data(cursor, product)
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter produto por código SKU: {e}") from e # Erro personalizado para erro de banco de dados

    def get_product_cards_by_name (self, name_product: str) -> Optional[List[ProductCardDict]]:
        """
        Obtém informações para poder montar os cards de produtos com o nome informado e que estão ativos.

        Args:
            name_product: Nome do produto a ser buscado.

        Returns:
            Optional[List[ProductCardDict]]: Lista com as informações dos cards correspondentes aos nomes informados ou None se não houver produtos com o nome informado.
        """

        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM products_card WHERE nome_produto LIKE ? AND ativo = 1"
                values = (f"%{name_product}%",)

                cursor.execute(query, values)

                products = cursor.fetchall()

                if len(products) > 0:
                    return [row_to_product_card_dict(row=product) for product in products]
                else:
                    return None

        except DatabaseError as e:
            raise DatabaseOperationError(f"Não foi possível localizar produtos com esse nome: {e}") from e # Erro personalizado para erro de banco de dados


    def get_all_product_cards_by_name(self, name_product: str) -> Optional[List[ProductCardDict]]:
        """

        Obtém as informações para poder montar os cards de produtos com o nome informado

        Args:
            name_product: Nome do produto a ser buscado.

        Returns:
            Optional[List[ProductCardDict]]: Lista com as informações dos cards correspondentes aos nomes informados ou None se não houver produtos com o nome informado.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM products_card WHERE nome_produto LIKE ?"
                values = (f"%{name_product}%",)

                cursor.execute(query, values)

                products = cursor.fetchall()

                if len(products) > 0:
                    return [row_to_product_card_dict(row=product) for product in products]
                else:
                    return None
                    
        except DatabaseError as e:
            raise DatabaseOperationError(f"Não foi possível localizar produtos com esse nome: {e}") from e # Erro personalizado para erro de banco de dados

    def get_active_product_cards_lower_minimum_balance(self) -> Optional[List[ProductCardDict]]:
        """
        Obtém as informações para os cards de produtos com saldo inferior ao saldo mínimo e que estão ativos.

        Args:
            None

        Returns:
            Optional[List[ProductCardDict]]: Lista com as informações dos cards correspondentes aos produtos com saldo inferior ao saldo mínimo ou None se não houver produtos com saldo inferior ao saldo mínimo.
        """

        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM products_card WHERE saldo_atual <= saldo_min * 1.5 AND ativo = 1"
                cursor.execute(query)

                products = cursor.fetchall()

                if len(products) > 0:
                    return [row_to_product_card_dict(row=product) for product in products]
                else:
                    return None
                    
        except DatabaseError as e:
            raise DatabaseOperationError(f"Não foi possível localizar produtos com saldo inferior ao saldo mínimo: {e}") from e # Erro personalizado para erro de banco de dados

## Funções auxiliares da aplicação
    def get_by_id(self, id: int) -> Optional[FullProductData]:
        """
        Obtém um produto pelo ID.

        Args:
            id: ID do produto a ser obtido.

        Returns:
            Optional[FullProductData]: Produto encontrado como objeto FullProductData ou None se não houver produto correspondente.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM products_information WHERE id_produto = ?"
                values = (id,)
                cursor.execute(query, values)
                product = cursor.fetchone()

                if product is None:
                    raise ProductNotFoundError(f"Produto com ID {id} não encontrado.")

                return row_to_full_product_data(cursor, product)
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter produto por ID: {e}") from e # Erro personalizado para erro de banco de dados
            
    def sku_exists(self, cod_sku: int) -> bool:
        """
        Verifica se o código SKU existe no banco de dados.

        Args:
            cod_sku: Código SKU a ser verificado.

        Returns:
            bool: True se o código SKU existe, False caso contrário.
        """
        try:
            self.get_by_cod_sku(cod_sku=cod_sku)   
            return True
        except ProductNotFoundError:
            return False

    def has_balance(self, id: int) -> bool:
        """
        Verifica se o produto possui saldo ativo.

        Args:
            id: ID do produto a ser verificado.

        Returns:
            bool: True se o produto possui saldo ativo, False caso contrário.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM saldo_produto WHERE id_produto = ?"
                values = (id,)
                cursor.execute(query, values)
                saldo = cursor.fetchone()

                if saldo is None:
                    return False
                return True

        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao verificar se o produto tem saldo: {e}") from e # Erro personalizado para erro de banco de dados