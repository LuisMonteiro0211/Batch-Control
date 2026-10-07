"""
Módulo de DTOs de produto.

Define estruturas imutáveis para transporte de dados de produtos
entre camadas (repository → service → GUI).
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from src.model.stock_level import StockLevel

@dataclass(frozen=True)
class _ProductBaseDTO:
    name: str
    minimun_balance: int
    product_firm: str
    product_code_chb: int
    consumption_monthly: float
    product_status: int
@dataclass(frozen=True)
class ProductCreateDTO(_ProductBaseDTO):
    """
    Classe base sem os campos opcionais (id, created_at, updated_at)
    """

@dataclass(frozen=True)
class ProductDTO(_ProductBaseDTO):
    """
    Dados completos de um produto para cadastro, edição e persistência.

    Campos opcionais (id, created_at, updated_at) são preenchidos
    apenas em produtos já existentes no banco.
    """

    id: int
    created_at: datetime
    updated_at: datetime
@dataclass(frozen=True)
class ProductCardDTO:
    """
    Dados resumidos de um produto para exibição na tabela de alertas.

    Inclui saldo atual e nível de estoque calculado para indicadores visuais.
    """

    product_id: int
    product_code_chb: int
    product_name: str
    product_firm: str
    minimun_balance: int
    current_balance: int
    status: int
    stock_level: Optional[StockLevel] = None


@dataclass(frozen=True)
class SearchObjectTransfer:
    product_cards: Optional[List[ProductCardDTO]]
    text_search: Optional[str]
