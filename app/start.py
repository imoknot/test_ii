from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine
from .models.modelsql import Base
from .settings import setting
from . import routes


# create Bases
async def async_create_base() -> None:
    engine = create_async_engine(setting.sql_async_connect, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


tags_metadata = [
    {"name": "main", "description": "Базовый АПИ"}
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title=setting.title_api,
    docs_url=setting.doc_url,
    version=setting.version)

# @app.on_event("startup")
# async def startup_event():
#     await async_create_base()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
