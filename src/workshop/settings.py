from pydantic import BaseSettings
from os.path import join, dirname


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./database.sqlite3'



settings = Settings(
    _env_file=join(dirname(__file__), '../.env'),
    _env_file_encoding='utf-8'
)