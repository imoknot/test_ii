from fastapi import APIRouter
from fastapi.responses import HTMLResponse

main_router = APIRouter()


@main_router.get('/', response_class=HTMLResponse, tags=['main'])
def read_root():
    return '<h1>¯\_(ツ)_/¯</h1>'
