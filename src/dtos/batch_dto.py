from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class BatchDTO:
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