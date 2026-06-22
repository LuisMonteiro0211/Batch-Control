from src.dtos.product_dto import ProductDTO
from typing import Any, Dict, List

from src.exceptions.exceptions import ValidationError
from src.helpers.helpers import is_number, is_valid_string, sanitize_string


NUMBER_FIELDS = ["minimun_balance", "product_code_chb", "consumption_monthly"]

def build_product_dto(raw_date: Dict[str, Any]) -> ProductDTO:
    required_fields: List[str] = [
        "name",
        "minimun_balance",
        "product_firm",
        "product_code_chb",
        "consumption_monthly",
    ]

    for name_field in required_fields:
        #For para pegar o valor de cada campo
        value = raw_date.get(name_field, "")

        if name_field in NUMBER_FIELDS:
            if not is_number(value=value):
            #Se o campo estiver na lista de campo numéricos e a função is_number retornar FALSE, lança um erro de validação
                raise ValidationError(f"O campo {name_field} deve ser um número!")

        else:
            if not is_valid_string(value=value):
                raise ValidationError(f"O campo {name_field} deve ser uma string válida!")


    return ProductDTO(
        name=sanitize_string(value=raw_date["name"]),
        minimun_balance=int(raw_date["minimun_balance"]),
        product_firm=sanitize_string(value=raw_date["product_firm"]),
        product_code_chb=int(raw_date["product_code_chb"]),
        consumption_monthly=float(raw_date["consumption_monthly"]),

        id=None,
        created_at=None,
        updated_at=None,
    )