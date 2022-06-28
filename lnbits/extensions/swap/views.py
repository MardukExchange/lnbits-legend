from fastapi import FastAPI, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from lnbits.core.models import User
from lnbits.decorators import check_user_exists

from . import swap_ext, swap_renderer

templates = Jinja2Templates(directory="templates")


@swap_ext.get("/", response_class=HTMLResponse)
async def index(request: Request, user: User = Depends(check_user_exists)):
    return swap_renderer().TemplateResponse(
        "swap/index.html", {"request": request, "user": user.dict()}
    )
