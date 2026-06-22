from src.exceptions.exceptions import InvalidDateError, ValidationError
from src.model.product import Product
from src.dtos.product_dto import ProductDTO
from typing import Any
from datetime import datetime

def row_to_dict(cursor: Any, row: tuple[Any, ...]) -> dict[str, Any]:
    """
    Converte uma linha retornada pelo SQLite (tuple) em dicionário.

    Args:
        cursor: Cursor usado na consulta (fornece os nomes das colunas).
        row: Tupla retornada por fetchone ou item de fetchall.

    Returns:
        dict[str, Any]: Linha convertida com chaves nomeadas pelas colunas.
    """
    columns = [column[0] for column in cursor.description]
    return dict(zip(columns, row))

def product_to_model(product: dict[str, Any]) -> Product:
    """
    Converte um dicionário de produto para um objeto Product.

    Args:
        product: Dicionário com os dados do produto.

    Returns:
        Product: Objeto Product com os valores do dicionário.
    """
    return Product(
        id=product.get("id_produto"),
        nome_produto=product["nome_produto"],
        empresa=product.get("empresa", ""),
        saldo_min=product.get("saldo_min", 0),
        cod_sku=product["cod_sku"],
        consumo_mensal=product.get("consumo_mensal", 0.0),
        ativo=bool(product.get("ativo", 1)),
        data_cadastro=product.get("data_cadastro"),
        data_atualizacao=product.get("data_atualizacao"),
    )

def is_number(value: str) -> bool:
    """
    Verifica se um valor é um número.

    Args:
        value: Valor a ser verificado.

    Returns:
        bool: True se o valor é um número, False caso contrário.
    """
    
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_space(value: str) -> bool:
    """
    Verifica se um valor é um espaço.

    Args:
        value: Valor a ser verificado.

    Returns:
        bool: True se o valor é um espaço, False caso contrário.
    """
    return value.isspace()

def is_empty(value: str) -> bool:
    """
    Verifica se um valor é vazio.

    Args:
        value: Valor a ser verificado.

    Returns:
        bool: True se o valor é vazio, False caso contrário.
    """
    return bool(value.isspace())

def is_valid_string(value: str) -> bool:
    """
    Verifica se um valor é um nome válido.

    Args:
        value: Valor a ser verificado.

    Returns:
        bool: True se o valor é um nome válido, False caso contrário.
    """
    if isinstance(value, int):
        return False

    return bool(value.strip())

def sanitize_string(value: str) -> str:
    """
    Sanitiza um valor de string. Remove espaços e converte para title case.

    Args:
        value: Valor a ser sanitizado.

    Returns:
        str: Valor sanitizado.
    """
    return value.strip().capitalize()

def sanitize_date(value: str) -> str:
    """
    Sanitiza uma data. Converte para o formato YYYY-MM-DD.

    Args:
        value: Valor a ser sanitizado.

    Returns:
        str: Valor sanitizado.
    """
    try:
        date = datetime.strptime(value, "%d/%m/%Y")
        if date > datetime.now():
            raise InvalidDateError(f"A data {value} é maior que a data atual {datetime.now().strftime('%d/%m/%Y')}" )
        return date.strftime("%Y-%m-%d")
    except ValueError as e:
        raise InvalidDateError(f"A data {value} é inválida: {e}") from e