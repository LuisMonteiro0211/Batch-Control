from tkinter import INSERT
from src.model.product import Product
from data.connection_db import get_connection
from src.interface.entity import Entity
from typing import Any, List, final, Optional, Tuple

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

        with get_connection(self._database_name) as cursor:
            query = "INSERT INTO produtos (nome_produto, empresa, saldo_min, cod_sku, consumo_mensal, ativo) VALUES (?, ?, ?, ?, ?, ?)"
            values = (entity.nome_produto, entity.empresa, entity.saldo_min, entity.cod_sku, entity.consumo_mensal, 1 if entity.ativo else 0)

            cursor.execute(query, values)

            return cursor.lastrowid if cursor.lastrowid is not None else None


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

        query = f"UPDATE produtos SET {", ".join(fields)} WHERE id = ?"

        values.append(id)

        with get_connection(self._database_name) as cursor:
            cursor.execute(query, values)
        

    def delete(self, id: int) -> None:
        """
        Deleta um produto no banco de dados.

        Args:
            id: ID do produto a ser deletado.

        Returns:
            None
        """
        with get_connection(self._database_name) as cursor:
            query = "DELETE FROM produtos WHERE id = ?"
            values = (id,)
            cursor.execute(query, values)

    def get_all(self) -> List[Any]:
        """
        Obtém todos os produtos do banco de dados.

        Args:
            None

        Returns:
            List[Any]: Lista de produtos.
        """

        with get_connection(self._database_name) as cursor:
            query = "SELECT * FROM produtos"
            cursor.execute(query)
            return cursor.fetchall()

    def get_by_id(self, id: int) -> Any:
        """
        Obtém um produto pelo ID do banco de dados.

        Args:
            id: ID do produto a ser obtido.

        Returns:
            Any: Produto encontrado.
        """
        with get_connection(self._database_name) as cursor:
            query = "SELECT * FROM produtos WHERE id = ?"
            values = (id,)

            cursor.execute(query, values)
            return cursor.fetchone()