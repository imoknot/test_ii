from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    sql_async_connect: str = 'postgresql+asyncpg://bd_user:user_pass@localhost/base_name'
    sql_connect: str = 'postgresql://bd_user:user_pass@localhost/base_name'
    title_api: str = 'Название АПИ'
    doc_url: str = '/docs'
    version: str = 'v0.1'


setting = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
