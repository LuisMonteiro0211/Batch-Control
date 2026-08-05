"""
Módulo de DTO de lote.

Define a estrutura imutável para transporte de dados de lotes
entre camadas (repository → service → GUI).
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class BatchDTO:
    """
    Dados completos de um lote para cadastro e persistência.

    Campos opcionais (id, created_at, updated_at) são preenchidos
    apenas em lotes já existentes no banco.
    """

    batch: str
    code_chb: str
    manufacturer_date: str
    expiration_date: str
    product_firm: str
    product: str
    quantity: str
    nf: str

    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
