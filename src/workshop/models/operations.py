from decimal import Decimal
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import date


class OperationKind(str, Enum):
    INCOME = 'income',
    OUTCOME = 'outcome'


class Operation(BaseModel):
    id: int
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

    class Config:
        orm_mode = True