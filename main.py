from typing import Union

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(
    request: Request,
):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/test2")
def read_root(
    request: Request,
):
    return templates.TemplateResponse("test2.html", {"request": request})