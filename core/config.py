from pydantic import BaseSettings
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    
    # Model base do SQLAlchemy.
    DBModelBase = declarative_base()

    # Prefixo da API
    API_V1_STR: str = '/api/v1'

    # URL do banco de dados.
    DB_URL: str = "postgresql+asyncpg://postgres:dev@localhost:5432/jornal"
    

    # Token ultilizando para criptografar e descriptografar o usuário.
    JWT_SECRET: str = 'uA-0eFxl3xI_AK01hoxNBpUcXzzJM3uU5VCeg0qQf3o'
    """
    # Gerar secrets

    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    
    ALGORITHM: str = 'HS256'

    # 60 minutos x 24 horas x 7 dias -> uma semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 

    
    class Config:
        case_sensitive = True

settings = Settings()