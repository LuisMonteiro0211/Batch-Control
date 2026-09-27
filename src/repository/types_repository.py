from typing import TypedDict

class FullProductData(TypedDict):
    """
    Formato de retorno para as consultas de produtos, seguindo o padrão da view de products_information

    - id_produto: ID do produto
    - nome_produto: Nome do produto
    - empresa: Empresa do produto
    - saldo_min: Saldo mínimo do produto
    - cod_sku: Código SKU do produto
    - consumo_mensal: Consumo mensal do produto
    - ativo: Ativo do produto
    - data_cadastro: Data de cadastro do produto
    - data_atualizacao: Data de atualização do produto
    - saldo_atual: Saldo atual do produto
    """


    id_produto: int
    nome_produto: str
    empresa: str
    saldo_min: int
    cod_sku: int
    consumo_mensal: int
    ativo: bool
    data_cadastro: str
    data_atualizacao: str
    saldo_atual: int


class ProductCardDict(TypedDict):
    """
    Formato padrão de resultado para chamadas de construção de cards de produtos
    Primeiro vem o card e depois todas as informações do produto

    
    - nome_produto: Nome do produto
    """

    id_produto: int
    codigo_sku: int
    nome_produto: str
    empresa: str
    saldo_min: int
    ativo: int
    saldo_atual: int