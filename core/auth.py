from pytz import timezone

from datetime import datetime
from datetime import timedelta

from typing import Optional
from typing import List
from pydantic import EmailStr

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from jose import jwt

from models.usuario_model import UsuarioModel
from core.config import settings
from core.security import verificar_senha


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/usuarios/login')

async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha):
            return None

        return usuario

def __criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:

    """https://www.rfc-editor.org/rfc/rfc7519"""

    payload = {}

    mt = timezone('America/Cuiaba')
    expira = datetime.now(tz=mt) + tempo_vida

    payload['type'] = tipo_token

    payload['exp'] = expira

    payload['iat'] = datetime.now(tz=mt)

    payload['sub'] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def criar_token_acesso(sub: str) -> str:

    """
    https://jwt.io
    """

    return __criar_token(
        tipo_token='acess_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )