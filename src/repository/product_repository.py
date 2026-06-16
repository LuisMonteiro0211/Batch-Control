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
)
from src.helpers.helpers import row_to_dict
from src.interface.entity import Entity
from src.model.product import Product

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

    def update(self, id: int, list_to_update: List[Tuple[str, Any]]) -> None:
        """
        Atualiza um produto no banco de dados.

        Args:
            id: ID do produto a ser atualizado.
            list_to_update: Lista de tuplas contendo o nome do campo e o valor a ser atualizado (ex: [("nome_produto", "Novo nome"), ("empresa", "Nova empresa")]).

        Returns:
            None
        """

        if not list_to_update:
            return

        fields = []
        values = []

        for field_name, value in list_to_update:
            fields.append(f"{field_name} = ?")
            values.append(value)

        query = f"UPDATE produtos SET {", ".join(fields)} WHERE id_produto = ?"

        values.append(id)

        try:
            with get_connection(self._database_name) as cursor:
                cursor.execute(query, values)
                
                if cursor.rowcount == 0:
                    raise ProductNotFoundError(f"Produto com ID {id} não encontrado.")

        except IntegrityError as e:
            for field_name, value in list_to_update:
                if field_name == "cod_sku":
                    raise DuplicateSkuError(value) from e # Erro personalizado para código SKU duplicado
                else:
                    raise DatabaseOperationError(f"Erro ao atualizar produto: {e}") from e # Erro personalizado para erro de banco de dados
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao atualizar produto: {e}") from e # Erro personalizado para erro de banco de dados

    def delete(self, id: int) -> None:
        """
        Deleta um produto no banco de dados.

        Args:
            id: ID do produto a ser deletado.

        Returns:
            None
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "DELETE FROM produtos WHERE id_produto = ?"
                values = (id,)
                cursor.execute(query, values)
                
                if cursor.rowcount == 0:
                    raise ProductNotFoundError(f"Produto com ID {id} não encontrado.")

        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao deletar produto: {e}") from e # Erro personalizado para erro de banco de dados

    def get_all(self) -> List[dict[str, Any]]:
        """
        Obtém todos os produtos do banco de dados.

        Args:
            None

        Returns:
            List[dict[str, Any]]: Lista de produtos como dicionários.
        """

        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM produtos"
                cursor.execute(query)
                products = cursor.fetchall()

                if not products:
                    raise ProductNotFoundError("Não há produtos cadastrados.")

                return [row_to_dict(cursor, product) for product in products]
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter todos os produtos: {e}") from e # Erro personalizado para erro de banco de dados

    def get_by_id(self, id: int) -> dict[str, Any]:
        """
        Obtém um produto pelo ID.

        Args:
            id: ID do produto a ser obtido.

        Returns:
            dict[str, Any]: Produto encontrado como dicionário.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM produtos WHERE id_produto = ?"
                values = (id,)
                cursor.execute(query, values)
                product = cursor.fetchone()

                if product is None:
                    raise ProductNotFoundError(f"Produto com ID {id} não encontrado.")

                return row_to_dict(cursor, product)
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter produto por ID: {e}") from e # Erro personalizado para erro de banco de dados

    def get_by_cod_sku(self, cod_sku: int) -> dict[str, Any]:
        """
        Obtém um produto pelo código SKU.

        Args:
            cod_sku: Código SKU do produto a ser obtido.

        Returns:
            dict[str, Any]: Produto encontrado como dicionário.
        """

        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM produtos WHERE cod_sku = ?"
                values = (cod_sku,)

                cursor.execute(query, values)
                product = cursor.fetchone()

                if product is None:
                    raise ProductNotFoundError(f"Produto com código SKU {cod_sku} não encontrado.")

                return row_to_dict(cursor, product)
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter produto por código SKU: {e}") from e # Erro personalizado para erro de banco de dados

    def get_by_nome_produto(self, nome_produto: str) -> dict[str, Any]:
        """
        Obtém um produto pelo nome do produto.

        Args:
            nome_produto: Nome do produto a ser obtido.

        Returns:
            dict[str, Any]: Produto encontrado como dicionário.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM produtos WHERE nome_produto = ?"
                values = (nome_produto,)
                cursor.execute(query, values)
                product = cursor.fetchone()

                if product is None:
                    raise ProductNotFoundError(f"Produto com nome {nome_produto} não encontrado.")

                return row_to_dict(cursor, product)
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter produto por nome: {e}") from e # Erro personalizado para erro de banco de dados


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

    def get_id_by_cod_sku(self, cod_sku: int) -> int:
        """
        Obtém o ID do produto pelo código SKU.

        Args:
            cod_sku: Código SKU a ser obtido.

        Returns:
            int: ID do produto.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT id_produto FROM produtos WHERE cod_sku = ?"
                values = (cod_sku,)

                cursor.execute(query, values)

                row = cursor.fetchone()

                if row is None:
                    raise ProductNotFoundError(f"Produto com código SKU {cod_sku} não encontrado.")

                return row_to_dict(cursor, row)["id_produto"]

        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao obter ID do produto por código SKU: {e}") from e # Erro personalizado para erro de banco de dados

    def search_by_name(self, name: str) -> Optional[List[dict[str, Any]]]:
        """
        Busca produtos pelo nome.

        Args:
            name: Nome do produto a ser buscado.

        Returns:
            List[dict[str, Any]]: Lista de produtos encontrados como dicionários.
        """
        try:
            with get_connection(self._database_name) as cursor:
                query = "SELECT * FROM produtos WHERE nome_produto LIKE ?"
                values = (f"%{name}%",)
                cursor.execute(query, values)
                products = cursor.fetchall()

                if not products:
                    raise ProductNotFoundError(f"Produto com nome {name} não encontrado.")

                return [row_to_dict(cursor, product) for product in products]
        except DatabaseError as e:
            raise DatabaseOperationError(f"Erro ao buscar produtos por nome: {e}") from e # Erro personalizado para erro de banco de dados