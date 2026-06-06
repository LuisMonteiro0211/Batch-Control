from dataclasses import dataclass
from token import OP
from typing import Optional
from datetime import datetime

@dataclass(frozen=True)
class Product:
    nome_produto: str
    empresa: str
    saldo_min: int
    cod_sku: int
    consumo_mensal: float

    id: Optional[int] = None
    ativo: Optional[bool] = True
    data_cadastro: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
