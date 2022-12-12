from typing import Generator, Optional
from pydantic import BaseModel

from core.database import Session
from core.auth import oauth2_schema
from core.config import settings

from models.usuario_model import UsuarioModel

from fastapi import Depends, HTTPException, status

from jose import jwt, JWTError

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class TokenData(BaseModel):
    username: Optional[str] = None

    
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session

    finally:
        await session.close()


async def get_current_user(token: str = Depends(oauth2_schema), db: AsyncSession = Depends(get_session)) -> UsuarioModel:

    credential_exeception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível autenticar a credencial.',
        headers={'WWW-Authenticate':'Bearer'}
        )

    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={'verify_aud': False}
            )

        username: str = payload.get('sub')

        if not username:
            raise credential_exeception

        token_data: TokenData = TokenData(username=username)
    
    except JWTError:
            raise credential_exeception

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == int(token_data.username))
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            raise credential_exeception

        return usuario