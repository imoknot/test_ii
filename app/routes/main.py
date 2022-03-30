from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get('/', response_class=HTMLResponse, tags=['main'])
def read_root():
    return '<h1>¯\_(ツ)_/¯</h1>'
