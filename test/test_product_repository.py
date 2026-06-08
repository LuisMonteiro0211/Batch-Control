import pytest

from src.exceptions import DuplicateSkuError, ProductNotFoundError
from src.model.product import Product
from src.repository.product_repository import ProductRepository

test_product_repository = ProductRepository("test_batch_control.db")

def test_create_product ():
    product = Product(
        nome_produto="Produto_teste",
        empresa="Empresa_teste",
        saldo_min=100,
        cod_sku=123456,
        consumo_mensal=1000,
    )
    result = test_product_repository.create(product)

    assert result is not None
    assert result > 0

    test_product_repository.delete(result)

def test_get_all_products():
    products = test_product_repository.get_all()

    assert products is not None
    assert len(products) >= 10


def test_get_product_by_id():
    product = test_product_repository.get_by_id(1)

    assert product is not None
    assert product["nome_produto"] == "Paracetamol 500mg"
    assert product["empresa"] == "Farmácia ABC"
    assert product["saldo_min"] == 100
    assert product["cod_sku"] == 1001
    assert product["consumo_mensal"] == 150.5

def test_get_product_by_cod_sku():
    product = test_product_repository.get_by_cod_sku(1001)

    assert product is not None
    assert product["nome_produto"] == "Paracetamol 500mg"
    assert product["empresa"] == "Farmácia ABC"
    assert product["saldo_min"] == 100
    assert product["cod_sku"] == 1001
    assert product["consumo_mensal"] == 150.5

def test_create_product_sku_duplicado():
    product = Product(
        nome_produto="Duplicado",
        empresa="Empresa_teste",
        saldo_min=1,
        cod_sku=1001,
        consumo_mensal=1,
    )

    with pytest.raises(DuplicateSkuError) as exc_info:
        test_product_repository.create(product)

    assert exc_info.value.cod_sku == 1001

def test_delete_product_nao_encontrado():
    with pytest.raises(ProductNotFoundError, match="ID 99999"):
        test_product_repository.delete(99999)

def test_update_product_nao_encontrado():
    with pytest.raises(ProductNotFoundError, match="ID 99999"):
        test_product_repository.update(99999, [("nome_produto", "Novo nome")])

def test_update_product_sku_duplicado():
    with pytest.raises(DuplicateSkuError) as exc_info:
        test_product_repository.update(1, [("cod_sku", 1010)])
    assert exc_info.value.cod_sku == 1010

def test_update_product_nao_encontrado():
    with pytest.raises(ProductNotFoundError, match="ID 99999"):
        test_product_repository.update(99999, [("nome_produto", "Novo nome")])