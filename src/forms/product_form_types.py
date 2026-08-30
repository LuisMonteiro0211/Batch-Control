from typing import TypedDict

class EditProductRawData(TypedDict):
    # Tudo é retornado em string, pois é o que vem do formulário sem tratamento
    nome_produto: str
    empresa: str
    saldo_min: str
    ativo: str

class NewProductRawData(TypedDict):
    # Padronização do nome dos campos do formulário de cadastro de novos produtos
    nome_produto: str
    saldo_min: str
    empresa: str
    cod_sku: str
    consumo_mensal: str