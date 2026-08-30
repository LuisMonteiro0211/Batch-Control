from src.helpers.helpers import diff_product_dto
from src.dtos.product_dto import ProductDTO
import pytest
from dataclasses import replace

def test_sucess_diff_product_dto():
    original_product_dto: ProductDTO = ProductDTO(
        name="Paracetamol 500mg",
        minimun_balance=100,
        product_firm="Farmácia ABC",
        product_code_chb=1001,
        consumption_monthly=150.5,
        product_status=1,
    )

    new_product_dto: ProductDTO = replace(
        original_product_dto,
        name="Paracetamol 1gm",
        minimun_balance=200,
        product_firm="Farmácia 2",
    )   
    
    diff_list = diff_product_dto(
        product_old=original_product_dto,
        product_new=new_product_dto
    )
    assert diff_list is not None
    assert diff_list == [
        ("nome_produto", "Paracetamol 1gm"),
        ("saldo_min", 200),
        ("empresa", "Farmácia 2"),
    ]
