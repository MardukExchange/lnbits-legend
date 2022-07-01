import json
from typing import Dict, List, Optional

from fastapi.params import Query
from pydantic.main import BaseModel
from sqlalchemy.engine import base  # type: ignore

class SubmarineSwap(BaseModel):
    id: str
    wallet: str
    amount: int
    time: int
    status: str
    refund_privkey: str
    boltz_id: str
    expected_amount: int
    timeout_block_height: int
    claim_address: str
    address: str
    # bip21: str
    redeem_script: str
    payment_hash: str

class CreateSubmarineSwap(BaseModel):
    wallet: str = Query(...)
    # amount: int = Query(..., ge=10000, le=4294967)
    amount: float = Query(...)
    base: str = Query(...)
    quote: str = Query(...)
    baseAmount: float = Query(...)
    quoteAmount: float = Query(...)

class ReverseSubmarineSwap(BaseModel):
    id: str
    wallet: str
    amount: int
    # onchain_address: str
    instant_settlement: bool
    claim_address: str
    refund_address: str
    time: int
    status: str
    boltz_id: str
    preimage: str
    claim_privkey: str
    lockup_address: str
    onchain_amount: int
    timeout_block_height: int
    redeem_script: str

class CreateReverseSubmarineSwap(BaseModel):
    wallet: str = Query(...)
    amount: float = Query(...)
    base: str = Query(...)
    quote: str = Query(...)
    baseAmount: float = Query(...)
    quoteAmount: float = Query(...)
    # amount: int = Query(..., ge=10000, le=4294967)
    instant_settlement: bool = Query(...)
    # validate on-address, bcrt1 for regtest addresses
    # onchain_address: str = Query(..., regex="^(bcrt1|bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$")
    claimAddress: str = Query(...)