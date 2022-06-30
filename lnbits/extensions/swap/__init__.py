from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_swap")

swap_ext: APIRouter = APIRouter(prefix="/swap", tags=["swap"])

swap_static_files = [
    {
        "path": "/swap/static",
        "app": StaticFiles(directory="lnbits/extensions/swap/static"),
        "name": "swap_static",
    }
]

def swap_renderer():
    return template_renderer(["lnbits/extensions/swap/templates"])


from .views import *  # noqa
from .views_api import *  # noqa
