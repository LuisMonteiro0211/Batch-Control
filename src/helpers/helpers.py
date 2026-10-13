from re import I
from src.dtos import ProductCardDTO
from src.exceptions.exceptions import InvalidDateError
from src.dtos.product_dto import ProductDTO
from typing import Any, List, Tuple
from datetime import date, datetime
from dataclasses import fields
from src.repository.types_repository import FullProductData, ProductCardDict
from typing import List

def row_to_full_product_data(cursor: Any, row: tuple[Any, ...]) -> FullProductData:
    """
    Converte uma linha retornada pelo SQLite (tuple) em dicionário FullProductData.

    Args:
        cursor: Cursor usado na consulta (fornece os nomes das colunas).
        row: Tupla retornada por fetchone ou item de fetchall.

    Returns:
        FullProductData: Objeto FullProductData com os valores da linha.
    """
    columns = [column[0] for column in cursor.description]
    return FullProductData(**dict(zip(columns, row)))

def current_balance_from_db(saldo_atual: int | None) -> int:
    """
    Normaliza o saldo atual vindo do banco para exibição e cálculo de nível de estoque.

    Produtos recém-cadastrados podem ter ``saldo_atual`` NULL na view; nesse caso
    tratamos como zero.

    Args:
        saldo_atual: Valor da coluna saldo_atual ou None.

    Returns:
        int: Saldo atual como inteiro (0 quando None).
    """
    return 0 if saldo_atual is None else int(saldo_atual)


def row_to_product_card_dict(row: tuple[Any, ...]) -> ProductCardDict:
    """
    Converte uma linha retornada pelo SQLite (tuple) em dicionário ProductCardDict.

    Args:
        cursor: Cursor usado na consulta (fornece os nomes das colunas).
        row: Tupla retornada por fetchone ou item de fetchall.

    Returns:
        ProductCardDict: Objeto ProductCardDict com os valores da linha.
    """
    (id_produto, cod_sku, nome_produto, empresa, saldo_min, ativo, saldo_atual) = row

    return ProductCardDict(
        id_produto=id_produto,
        codigo_sku=cod_sku,
        nome_produto=nome_produto,
        empresa=empresa,
        saldo_min=saldo_min,
        ativo=ativo,
        saldo_atual=saldo_atual
    )

def dict_to_product_dto(product: FullProductData) -> ProductDTO:
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
        created_at=datetime.strptime(product["data_cadastro"], "%Y-%m-%d %H:%M:%S"),#Conversão para um objeto datetime
        updated_at=datetime.strptime(product["data_atualizacao"], "%Y-%m-%d %H:%M:%S"),#Conversão para um objeto datetime
    )

def dict_to_product_card_dto(product: ProductCardDict) -> ProductCardDTO:
    """
    Converte um dicionário de produto para um objeto ProductCardDTO.

    Args:
        product: Dicionário com os dados do produto.

    Returns:
        ProductCardDTO: Objeto ProductCardDTO com os valores do dicionário.
    """
    return ProductCardDTO(
        product_id=int(product.get("id_produto")),
        product_code_chb=int(product["codigo_sku"]),
        product_name=str(product["nome_produto"]),
        product_firm=str(product["empresa"]),
        minimun_balance=int(product["saldo_min"]),
        current_balance=current_balance_from_db(product["saldo_atual"]),
        status=int(product.get("ativo")),
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
    Sanitiza um valor de string. Remove espaços e converte para uppercase.

    Args:
        value: Valor a ser sanitizado.

    Returns:
        str: Valor sanitizado.
    """
    return value.strip().upper()

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

    DATABASE_COLUMNS = {
        "name": "nome_produto",
        "minimun_balance": "saldo_min",
        "product_firm": "empresa",
        "product_status": "ativo"
    }

    diff_list: List[Tuple[str, Any]]= []

    for field in fields(product_old):
        if field.name not in EDITABLE_FIELDS:
            continue

        else:
            old_value = getattr(product_old, field.name) #getattr acessa o atributo do objeto com o nome do campo sendo string e não .name
            new_value = getattr(product_new, field.name)

            if old_value != new_value:
                tuple_to_update: Tuple[str, Any] = (DATABASE_COLUMNS[field.name], new_value)
                diff_list.append(tuple_to_update)

    return diff_list

