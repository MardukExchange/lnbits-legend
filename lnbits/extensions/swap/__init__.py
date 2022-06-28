from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_swap")

swap_ext: APIRouter = APIRouter(prefix="/swap", tags=["swap"])


def swap_renderer():
    return template_renderer(["lnbits/extensions/swap/templates"])


from .views import *  # noqa
from .views_api import *  # noqa
