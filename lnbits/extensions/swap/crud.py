from http import HTTPStatus
from typing import List, Optional, Union

from starlette.exceptions import HTTPException

from .swap import (
    create_swap,
    create_reverse_swap,
    get_update_swap_status,
)
from lnbits.helpers import urlsafe_short_hash

from . import db
from .models import (
    CreateSubmarineSwap,
    SubmarineSwap,
    CreateReverseSubmarineSwap,
    ReverseSubmarineSwap,
)


"""
Submarine Swaps
"""
async def get_submarine_swaps(wallet_ids: Union[str, List[str]]) -> List[SubmarineSwap]:
    if isinstance(wallet_ids, str):
        wallet_ids = [wallet_ids]

    q = ",".join(["?"] * len(wallet_ids))
    rows = await db.fetchall(
        f"SELECT * FROM swap.submarineswap WHERE wallet IN ({q}) order by time DESC", (*wallet_ids,)
    )

    return [SubmarineSwap(**row) for row in rows]

async def update_submarine_swap_status(swap_id):
    await get_update_swap_status(swap_id)

async def get_submarine_swap(swap_id) -> SubmarineSwap:
    row = await db.fetchone("SELECT * FROM swap.submarineswap WHERE id = ?", (swap_id,))
    return SubmarineSwap(**row) if row else None

async def create_submarine_swap(data: CreateSubmarineSwap) -> Optional[SubmarineSwap]:

    swap_id = urlsafe_short_hash()
    swap = await create_swap(swap_id, data)
    await db.execute(
        """
        INSERT INTO swap.submarineswap (
            id,
            wallet,
            status,
            boltz_id,
            refund_privkey,
            expected_amount,
            timeout_block_height,
            address,
            claim_address,
            redeem_script,
            amount,
            payment_hash
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            swap_id,
            swap.wallet,
            swap.status,
            swap.boltz_id,
            swap.refund_privkey,
            swap.expected_amount,
            swap.timeout_block_height,
            swap.address,
            swap.claim_address,
            swap.redeem_script,
            swap.amount,
            swap.payment_hash,
        )
    )
    return await get_submarine_swap(swap_id)

async def delete_submarine_swap(swap_id):
    await db.execute("DELETE FROM swap.submarineswap WHERE id = ?", (swap_id,))



"""
Reverse Submarine Swaps
"""
async def get_reverse_submarine_swaps(wallet_ids: Union[str, List[str]]) -> List[ReverseSubmarineSwap]:
    if isinstance(wallet_ids, str):
        wallet_ids = [wallet_ids]

    q = ",".join(["?"] * len(wallet_ids))
    rows = await db.fetchall(
        f"SELECT * FROM swap.reverse_submarineswap WHERE wallet IN ({q}) order by time DESC", (*wallet_ids,)
    )

    return [ReverseSubmarineSwap(**row) for row in rows]

async def get_reverse_submarine_swap(swap_id) -> ReverseSubmarineSwap:
    row = await db.fetchone("SELECT * FROM swap.reverse_submarineswap WHERE id = ?", (swap_id,))
    return ReverseSubmarineSwap(**row) if row else None

async def create_reverse_submarine_swap(data: CreateReverseSubmarineSwap) -> Optional[ReverseSubmarineSwap]:

    swap_id = urlsafe_short_hash()
    swap = await create_reverse_swap(swap_id, data)
    # onchain_address, removed
    await db.execute(
        """
        INSERT INTO swap.reverse_submarineswap (
            id,
            wallet,
            status,
            boltz_id,
            instant_settlement,
            preimage,
            claim_privkey,
            lockup_address,
            onchain_amount,
            claim_address,
            refund_address,
            timeout_block_height,
            redeem_script,
            amount
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            swap_id,
            swap.wallet,
            swap.status,
            swap.boltz_id,
            swap.instant_settlement,
            swap.preimage,
            swap.claim_privkey,
            swap.lockup_address,
            swap.onchain_amount,
            # swap.onchain_address,
            swap.claim_address,
            swap.refund_address,
            swap.timeout_block_height,
            swap.redeem_script,
            swap.amount
        )
    )
    return await get_reverse_submarine_swap(swap_id)

async def delete_reverse_submarine_swap(swap_id):
    await db.execute("DELETE FROM swap.reverse_submarineswap WHERE id = ?", (swap_id,))

async def update_swap_status(swap: Union[ReverseSubmarineSwap, SubmarineSwap], status: str):
    if type(swap) == SubmarineSwap:
        await db.execute("UPDATE swap.submarineswap SET status='"+status+"' WHERE id='"+swap.id+"'")
    if type(swap) == ReverseSubmarineSwap:
        await db.execute("UPDATE swap.reverse_submarineswap SET status='"+status+"' WHERE id='"+swap.id+"'")
    return swap