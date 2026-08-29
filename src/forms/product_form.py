"""
Módulo de validação e construção de ProductDTO a partir de dados brutos do formulário.
"""

from dataclasses import replace
from src.dtos.product_dto import ProductDTO
from typing import Any, Dict, List
from src.forms.product_form_types import EditProductRawData, NewProductRawData
from src.exceptions.exceptions import ValidationError
from src.helpers.helpers import is_number, is_valid_string, sanitize_string


NUMBER_FIELDS = ["saldo_min", "cod_sku", "consumo_mensal"]


def build_product_dto(raw_data: NewProductRawData) -> ProductDTO:
    """
    Valida os campos do formulário e constrói um ProductDTO.

    Args:
        raw_data: Dicionário com os valores brutos coletados dos campos do formulário.
            Chaves esperadas: name, minimun_balance, product_firm,
            product_code_chb, consumption_monthly.

    Returns:
        ProductDTO validado e sanitizado, pronto para persistência.

    Raises:
        ValidationError: Se algum campo obrigatório estiver ausente ou inválido.
    """
    required_fields: List[str] = [
        "nome_produto",
        "saldo_min",
        "empresa",
        "cod_sku",
        "consumo_mensal",
    ]

    for name_field in required_fields:
        value = raw_data.get(name_field, "")

        if name_field in NUMBER_FIELDS:
            if not is_number(value=value):
                raise ValidationError(f"O campo {name_field} deve ser um número!")

        else:
            if not is_valid_string(value=value):
                raise ValidationError(f"O campo {name_field} deve ser uma string válida!")

    return ProductDTO(
        name=sanitize_string(value=raw_data["nome_produto"]),
        minimun_balance=int(raw_data["saldo_min"]),
        product_firm=sanitize_string(value=raw_data["empresa"]),
        product_code_chb=int(raw_data["cod_sku"]),
        consumption_monthly=float(raw_data["consumo_mensal"]),
        product_status=1,
        
        id=None,
        created_at=None,
        updated_at=None,

    )

def build_edit_product_dto(raw_data_edit: EditProductRawData, original_product_dto: ProductDTO) -> ProductDTO:
    """
    Constrói uma nova versão do ProductDTO mesclando valores editados com os originais.

    Args:
        raw_data_edit: Dicionário com os valores brutos coletados do formulário de edição.
        original_product_dto: ProductDTO original a ser editado.

    Returns:
        ProductDTO com os campos editáveis atualizados; demais campos herdados do original.
    """
    #Inicio das validações
    if not is_valid_string(value=raw_data_edit["nome_produto"]):
        raise ValidationError("O campo Nome do Produto deve ser uma string válida!")
    
    if not is_valid_string(value=raw_data_edit["empresa"]):
        raise ValidationError("O campo Empresa deve ser uma string válida!")

    if not is_number(raw_data_edit["saldo_min"]):
        raise ValidationError("O campo Saldo Mínimo deve ser um número!")

    return replace(
        original_product_dto,
        name=sanitize_string(value=raw_data_edit["nome_produto"]),
        product_firm=sanitize_string(value=raw_data_edit["empresa"]),
        minimun_balance=int(raw_data_edit["saldo_min"]),
        product_status=1 if raw_data_edit["ativo"] == "Ativo" else 0,
    )
