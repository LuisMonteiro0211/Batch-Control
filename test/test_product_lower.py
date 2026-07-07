import pytest

from src.model.stock_level import StockLevel
from src.repository.product_repository import ProductRepository
from src.service.product_service import ProductService

test_product_repository = ProductRepository("test_batch_control.db")
test_product_service = ProductService(test_product_repository)

def test_product_lower():
    products_lower = test_product_repository.get_product_lower_minimum_balance()

    assert products_lower is not None

    product = products_lower[1]

    assert product["nome_produto"] == "Amoxicilina 500mg"
    assert product["cod_sku"] == 1003
    assert product["empresa"] == "Laboratório XYZ"
    assert product["saldo_min"] == 9999
    assert product["estoque_atual"] == 940
    assert product["estoque_atual"] < product["saldo_min"]
    assert product["ativo"] == 1

def test_product_lower_service():
    products_lower = test_product_service.get_product_lower_minimum_balance()

    assert products_lower is not None

    product = products_lower[1]

    assert product.product_name == "Amoxicilina 500mg"
    assert product.product_code_chb == 1003
    assert product.product_firm == "Laboratório XYZ"
    assert product.minimun_balance == 9999
    assert product.stock_level == StockLevel.CRITICO


def test_product_lower_service_with_stock_level_alert():
    products_lower = test_product_service.get_product_lower_minimum_balance()

    assert products_lower is not None

    product = products_lower[0]

    assert product.product_name == "Produto Teste 1.5x Mínimo"
    assert product.product_code_chb == 999001
    assert product.product_firm == "Empresa Teste"
    assert product.minimun_balance == 100
    assert product.stock_level == StockLevel.ALERTA