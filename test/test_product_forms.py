from src.forms.product_form import build_product_dto
from src.dtos.product_dto import ProductDTO
from src.exceptions.exceptions import ValidationError
import pytest

def test_sucess_build_product_dto():
    raw_data = {
        "name": "Paracetamol 500mg",
        "minimun_balance": "100",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "1001",
        "consumption_monthly": 150.5,
    }
    product_dto: ProductDTO = build_product_dto(raw_data)
    assert product_dto is not None
    assert product_dto.name == "Paracetamol 500mg"
    assert product_dto.minimun_balance == 100

def test_error_build_product_dto_name_invalid():
    raw_data = {
        "name": 123,
        "minimun_balance": "100",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "1001",
        "consumption_monthly": 150.5,
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_minimun_balance_invalid():
    raw_data = {
        "name": "Paracetamol 500mg",
        "minimun_balance": "abcc",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "1001",
        "consumption_monthly": 150.5,
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_product_firm_invalid():
    raw_data = {
        "name": "Paracetamol 500mg",
        "minimun_balance": "100",
        "product_firm": 123,
        "product_code_chb": "1001",
        "consumption_monthly": 150.5,
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_product_code_chb_invalid():
    raw_data = {
        "name": "Paracetamol 500mg",
        "minimun_balance": "100",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "nnnnn",
        "consumption_monthly": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_consumption_monthly_invalid():
    raw_data = {
        "name": "Paracetamol 500mg",
        "minimun_balance": "100",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "1001",
        "consumption_monthly": "Aaaaa",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_build_product_dto_all_fields_invalid():
    raw_data = {
        "name": 123,
        "minimun_balance": "100",
        "product_firm": 123,
        "product_code_chb": "1001",
        "consumption_monthly": "150.5",
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_space_in_name():
    raw_data = {
        "name": "    ",
        "minimun_balance": "100",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "1001",
        "consumption_monthly": 150.5,
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_space_in_product_firm():
    raw_data = {
        "name": "Paracetamol 500mg",
        "minimun_balance": "100",
        "product_firm": "    ",
        "product_code_chb": "1001",
        "consumption_monthly": 150.5,
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_space_in_product_code_chb():
    raw_data = {
        "name": "Paracetamol 500mg",
        "minimun_balance": "100",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "    ",
        "consumption_monthly": 150.5,
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)

def test_error_empty_in_name():
    raw_data = {
        "name": "",
        "minimun_balance": "100",
        "product_firm": "Farmácia ABC",
        "product_code_chb": "1001",
        "consumption_monthly": 150.5,
    }
    with pytest.raises(ValidationError):
        build_product_dto(raw_data)