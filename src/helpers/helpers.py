from src.dtos import ProductCardDTO
from src.exceptions.exceptions import InvalidDateError
from src.dtos.product_dto import ProductDTO
from typing import Any, List, Tuple
from datetime import datetime
from dataclasses import fields

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

def dict_to_product_dto(product: dict[str, Any]) -> ProductDTO:
    """
    Converte um dicionário de produto para um objeto ProductDTO.

    Args:
        product: Dicionário com os dados do produto.

    Returns:
        ProductDTO: Objeto ProductDTO com os valores do dicionário.
    """
    return ProductDTO(
        name=str(product["nome_produto"]),
        minimun_balance=int(product["saldo_min"]),
        product_firm=str(product.get("empresa", "")),
        product_code_chb=int(product["cod_sku"]),
        consumption_monthly=float(product.get("consumo_mensal", 0.0)),
        product_status=int(product["ativo"]),
        id=int(product["id_produto"]),
        created_at=product.get("data_cadastro"),
        updated_at=product.get("data_atualizacao"),
    )

def dict_to_product_card_dto(product: dict[str, Any]) -> ProductCardDTO:
    """
    Converte um dicionário de produto para um objeto ProductCardDTO.

    Args:
        product: Dicionário com os dados do produto.

    Returns:
        ProductCardDTO: Objeto ProductCardDTO com os valores do dicionário.
    """
    return ProductCardDTO(
        product_id=int(product["id_produto"]),
        product_code_chb=int(product["cod_sku"]),
        product_name=str(product["nome_produto"]),
        product_firm=str(product["empresa"]),
        minimun_balance=int(product["saldo_min"]),
        current_balance=int(product["estoque_atual"]),
        status=int(product["ativo"]),
        stock_level=None,
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
    return value.strip().title()

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

def diff_product_dto(product_old: ProductDTO, product_new: ProductDTO) -> List[Tuple[str, Any]]:

    """
    Compara dois objetos (Somente campos onde a edição é permitida) e retorna uma lista de tuplas com os campos que foram alterados.

    """
    EDITABLE_FIELDS = [
        "name",
        "minimun_balance",
        "product_firm",
        "product_status"
    ]

    diff_list = []

    for field in fields(product_old):
        if field.name not in EDITABLE_FIELDS:
            continue

        else:
            old_value = getattr(product_old, field.name) #getattr acessa o atributo do objeto com o nome do campo sendo string e não .name
            new_value = getattr(product_new, field.name)

            if old_value != new_value:
                diff_list.append((field.name, new_value))

    return diff_list

