from pydantic import BaseModel

class Transaction(BaseModel):
    timestamp: str
    sender: int
    receiver: int
    remark: str
    amount: float
    type: str



