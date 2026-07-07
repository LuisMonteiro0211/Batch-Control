from enum import Enum

class StockLevel(Enum):
    NORMAL = "NORMAL"
    ALERTA = "ALERTA"
    CRITICO = "CRITICO"
    SEM_ESTOQUE = "SEM ESTOQUE"


def sort_level(current_stock: int, min_stock: int) -> StockLevel:
    """
    Função de classificação de nível de estoque.
    - Critico: Quando o saldo atual é menor ou igual ao saldo mínimo.
    - Alerta: Quando o saldo atual é menor ou igual a 1.5 vezes o saldo mínimo.
    - Normal: Quando o saldo atual é maior que 1.5 vezes o saldo mínimo.
    - Sem estoque: Quando o saldo atual é 0.
    
    Args:
        saldo_atual: int
        saldo_min: int

    Returns:
        StockLevel: Nível de estoque.
    """

    if current_stock == 0:
        return StockLevel.SEM_ESTOQUE
    
    if current_stock <= min_stock:
        return StockLevel.CRITICO

    if current_stock <= min_stock * 1.5:
        return StockLevel.ALERTA


    return StockLevel.NORMAL