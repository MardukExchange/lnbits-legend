import time
from mock import AsyncMock
from lnbits import bolt11
from lnbits.wallets.base import (
    StatusResponse,
    InvoiceResponse,
    PaymentResponse,
    PaymentStatus,
    Wallet,
)
from lnbits.settings import WALLET

from lnbits.wallets.fake import FakeWallet

from .helpers import get_random_string


# generates an invoice with FakeWallet
async def generate_mock_invoice(**x):
    invoice = await FakeWallet.create_invoice(
        FakeWallet(), amount=10, memo=f"mock invoice {get_random_string()}"
    )
    return invoice


WALLET.status = AsyncMock(
    return_value=StatusResponse(
        "",  # no error
        1000000,  # msats
    )
)

WALLET.create_invoice = generate_mock_invoice

# NOTE: This mock fails since it yields the same invoice multiple
# times which makes the db throw an error due to uniqueness contraints
# on the checking ID

# # primitive event loop for generate_mock_invoice()
# def drive(c):
#     while True:
#         try:
#             c.send(None)
#         except StopIteration as e:
#             return e.value

# # finally we await it
# invoice = drive(generate_mock_invoice())

# WALLET.create_invoice = AsyncMock(
#     return_value=InvoiceResponse(
#         True,  # ok
#         invoice.checking_id,  # checking_id (i.e. payment_hash)
#         invoice.payment_request,  # payment_request
#         "",  # no error
#     )
# )


def pay_invoice_side_effect(
    payment_request: str, fee_limit_msat: int
) -> PaymentResponse:
    invoice = bolt11.decode(payment_request)
    return PaymentResponse(
        True,  # ok
        invoice.payment_hash,  # checking_id (i.e. payment_hash)
        0,  # fee_msat
        "",  # no error
    )


WALLET.pay_invoice = AsyncMock(side_effect=pay_invoice_side_effect)
WALLET.get_invoice_status = AsyncMock(
    return_value=PaymentStatus(
        True,  # paid
    )
)
WALLET.get_payment_status = AsyncMock(
    return_value=PaymentStatus(
        True,  # paid
    )
)
