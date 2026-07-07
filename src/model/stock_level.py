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

TRANSACOES_PERMITIDAS = {
    StockLevel.NORMAL: {StockLevel.ALERTA, StockLevel.CRITICO, StockLevel.SEM_ESTOQUE},
    StockLevel.ALERTA: {StockLevel.CRITICO, StockLevel.NORMAL, StockLevel.SEM_ESTOQUE},
    StockLevel.CRITICO: {StockLevel.SEM_ESTOQUE, StockLevel.NORMAL, StockLevel.ALERTA},
    StockLevel.SEM_ESTOQUE: {StockLevel.NORMAL, StockLevel.ALERTA, StockLevel.CRITICO}
}

def can_perform_transaction(of_level: StockLevel, for_level: StockLevel) -> bool:
    """
    Função de verificação de permissão de transação.
    - Permite: Quando o nível de estoque atual é maior ou igual ao nível de estoque para o qual a transação está sendo realizada.
    - Não permite: Quando o nível de estoque atual é menor que o nível de estoque para o qual a transação está sendo realizada.

    Args:
        of_level: StockLevel
        for_level: StockLevel

    Returns:
        bool: True se a transação é permitida, False caso contrário.
    """
    return for_level in TRANSACOES_PERMITIDAS.get(of_level, set()) # Caso o método get não localize nada, o retorno padrão será o set vazio.