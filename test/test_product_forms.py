from src.forms.product_form import build_product_dto, build_edit_product_dto
from src.dtos.product_dto import ProductDTO
from src.exceptions.exceptions import ValidationError
from src.forms.product_form_types import NewProductRawData, EditProductRawData
import pytest

def test_sucess_build_product_dto():
    raw_data: NewProductRawData = {
        "nome_produto": "Paracetamol 500mg",
        "saldo_min": "100",
        "empresa": "Farmácia ABC",
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    product_dto: ProductDTO = build_product_dto(raw_data)
    assert product_dto is not None
    assert product_dto.name == "Paracetamol 500Mg"
    assert product_dto.minimun_balance == 100

def test_error_build_product_dto_name_invalid():
    raw_data: NewProductRawData = {
        "nome_produto": 123,
        "saldo_min": "100",
        "empresa": "Farmácia ABC",
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_minimun_balance_invalid():
    raw_data: NewProductRawData = {
        "nome_produto": "Paracetamol 500mg",
        "saldo_min": "abcc",
        "empresa": "Farmácia ABC",
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_product_firm_invalid():
    raw_data: NewProductRawData = {
        "nome_produto": "Paracetamol 500mg",
        "saldo_min": "100",
        "empresa": 123,
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_product_code_chb_invalid():
    raw_data: NewProductRawData = {
        "nome_produto": "Paracetamol 500mg",
        "saldo_min": "100",
        "empresa": "Farmácia ABC",
        "cod_sku": "nnnnn",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_consumption_monthly_invalid():
    raw_data: NewProductRawData = {
        "nome_produto": "Paracetamol 500mg",
        "saldo_min": "100",
        "empresa": "Farmácia ABC",
        "cod_sku": "1001",
        "consumo_mensal": "Aaaaa",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_all_fields_invalid():
    raw_data: NewProductRawData = {
        "name": 123,
        "saldo_min": "100",
        "empresa": 123,
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_space_in_name():
    raw_data: NewProductRawData = {
        "nome_produto": "    ",
        "saldo_min": "100",
        "empresa": "Farmácia ABC",
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_space_in_product_firm():
    raw_data: NewProductRawData = {
        "nome_produto": "Paracetamol 500mg",
        "saldo_min": "100",
        "empresa": "    ",
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_space_in_product_code_chb():
    raw_data: NewProductRawData = {
        "nome_produto": "Paracetamol 500mg",
        "saldo_min": "100",
        "empresa": "Farmácia ABC",
        "cod_sku": "    ",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_empty_in_name():
    raw_data: NewProductRawData = {
        "nome_produto": "",
        "saldo_min": "100",
        "empresa": "Farmácia ABC",
        "cod_sku": "1001",
        "consumo_mensal": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)


# ------------------------------------------------------------------------------------------------
# Testes de edição de produtos
# ------------------------------------------------------------------------------------------------

original_product_dto: ProductDTO = ProductDTO(
    name="Paracetamol 500mg",
    minimun_balance=100,
    product_firm="Farmácia ABC",
    product_code_chb=1001,
    consumption_monthly=150.5,
    product_status=1,
)

def test_sucess_build_edit_product_dto():
    raw_data: EditProductRawData = {
        "nome_produto": "Paracetamol 1gm",
        "saldo_min": "200",
        "ativo": "Inativo",
        "empresa": "Farmácia 2",
    }
    
    edited_product_dto: ProductDTO = build_edit_product_dto(
        raw_data_edit=raw_data,
        original_product_dto=original_product_dto
    )

    assert edited_product_dto is not None
    assert edited_product_dto.name == "Paracetamol 1Gm"
    assert edited_product_dto.minimun_balance == 200
    assert edited_product_dto.product_firm == "Farmácia 2"
    assert edited_product_dto.product_code_chb == 1001
    assert edited_product_dto.consumption_monthly == 150.5
    assert edited_product_dto.product_status == 0


def test_error_build_edit_product_dto_name_invalid():
    raw_data: EditProductRawData = {
        "nome_produto": 123,
        "saldo_min": "200",
        "ativo": "Inativo",
        "empresa": "Farmácia 2",
    }
    with pytest.raises(ValidationError):
        build_edit_product_dto(raw_data_edit=raw_data, original_product_dto=original_product_dto)

def test_error_build_edit_product_dto_minimun_balance_invalid():
    raw_data: EditProductRawData = {
        "nome_produto": "Paracetamol 1gm",
        "saldo_min": "abcc",
        "ativo": "Inativo",
        "empresa": "Farmácia 2",
    }
    with pytest.raises(ValidationError):
        build_edit_product_dto(raw_data_edit=raw_data, original_product_dto=original_product_dto)
        
def test_error_build_edit_product_dto_product_firm_invalid():
    raw_data: EditProductRawData = {
        "nome_produto": "Paracetamol 1gm",
        "saldo_min": "200",
        "ativo": "Inativo",
        "empresa": 123,
    }
    with pytest.raises(ValidationError):
        build_edit_product_dto(raw_data_edit=raw_data, original_product_dto=original_product_dto)
