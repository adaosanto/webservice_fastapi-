from pydantic import BaseModel, HttpUrl, validator
from typing import Optional

class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    url_fonte: HttpUrl
    descricao: str
    usuario_id: Optional[int]

    @validator('titulo')
    def titulo_tamanho(cls, v):
        if len(v) > 45:
            raise ValueError('O titulo deve conter menos que 46 caracteres.')

        return v

    @validator('url_fonte')
    def url_fonte_tamanho(cls, v):
        if len(v) > 256:
            raise ValueError('O valor deve conter menos que 256 caracteres.')

        return v

    class Config:
        orm_mode = True

class ArtigoSchemaUp(ArtigoSchema):
    id: Optional[int] = None
    titulo: Optional[str] = None
    url_fonte: Optional[HttpUrl] = None
    descricao: Optional[str] = None
    usuario_id: Optional[int] = None