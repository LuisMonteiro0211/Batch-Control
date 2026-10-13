from enum import Enum

class StockLevel(Enum):
    NORMAL = "NORMAL"
    ALERTA = "ALERTA"
    CRITICO = "CRITICO"
    SEM_ESTOQUE = "SEM ESTOQUE"


def sort_level(current_stock: int, min_stock: int) -> StockLevel:
    """
    Função de classificação de nível de estoque.
    - Critico: Saldo zero ou saldo atual menor ou igual ao saldo mínimo.
    - Alerta: Saldo acima do mínimo e menor ou igual a 1,5 vezes o saldo mínimo.
    - Normal: Saldo acima de 1,5 vezes o saldo mínimo.

    Args:
        current_stock: Saldo atual do produto.
        min_stock: Saldo mínimo configurado.

    Returns:
        StockLevel: Nível de estoque.
    """

    if current_stock == 0:
        return StockLevel.CRITICO
    
    if current_stock <= min_stock:
        return StockLevel.CRITICO

    if current_stock <= min_stock * 1.5:
        return StockLevel.ALERTA


    return StockLevel.NORMAL