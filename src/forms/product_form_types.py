from typing import TypedDict

class EditProductRawData(TypedDict):
    # Tudo é retornado em string, pois é o que vem do formulário sem tratamento
    nome_produto: str
    empresa: str
    saldo_min: str
    ativo: str
