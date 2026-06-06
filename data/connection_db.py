"""
Módulo de conexão com o banco de dados.

Uso recomendado:
>>> from connection_db import get_connection

>>> with get_connection("database.db") as cursor:
...     cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

print(users)

Observações:
    - O cursor é um objeto que permite executar comandos SQL no banco de dados.
    - O cursor é um objeto que permite fazer fetch dos resultados da consulta.
    - O cursor é um objeto que permite fechar a conexão com o banco de dados.
"""

from sqlite3 import connect, DatabaseError
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def get_connection(database_name: str):
    """
    Função para obter uma conexão com o banco de dados.

    Args:
        database_name: Nome do banco de dados.

    Returns:
        cursor: Cursor para executar comandos SQL no banco de dados.

    Raises:
        DatabaseError: Erro ao conectar ao banco de dados.

    Exemplo de uso:
    >>> with get_connection("database.db") as cursor:
    ...     cursor.execute("SELECT * FROM users")
    ...     users = cursor.fetchall()
    ...
    >>> print(users)
    """
    path_db = Path(__file__).parent / database_name
    cursor = None
    connection = None

    try:
        connection = connect(path_db)
        cursor = connection.cursor()
        yield cursor

    except DatabaseError as e:
        raise DatabaseError(f"Erro ao conectar ao banco de dados: {e}")

    finally:

        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
