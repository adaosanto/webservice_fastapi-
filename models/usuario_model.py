from core.config import settings
import sqlalchemy as sqa
import sqlalchemy.orm as orm

class UsuarioModel(settings.DBModelBase):
    
    __tablename__ = 'usuarios'

    id: int = sqa.Column(sqa.Integer, autoincrement=True, primary_key=True)
    nome: str = sqa.Column(sqa.String(256), nullable=True)
    sobrenome: str = sqa.Column(sqa.String(256), nullable=True)
    email: str = sqa.Column(sqa.String(256), nullable=False, index=True, unique=True)
    senha: str = sqa.Column(sqa.String(256), nullable=False)
    eh_admin: bool = sqa.Column(sqa.Boolean, default=False)
    artigos = orm.relationship(
        'ArtigoModel',
        cascade='all, delete-orphan',
        back_populates='criador',
        uselist=True,
        lazy='joined'
    )