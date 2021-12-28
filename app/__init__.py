from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {"name": "users", "description": "Hello user!"},
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="Suslig API",
    description='Fast and light',
    version="1.0")

from fastapi.staticfiles import StaticFiles

from .routes import login


app.include_router(login.login_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images/", StaticFiles(directory="images"), name="images")
