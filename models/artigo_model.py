import sqlalchemy as sqa
import sqlalchemy.orm as orm
from core.config import settings

class ArtigoModel(settings.DBModelBase):
    
    __tablename__ = 'artigos'

    id: int = sqa.Column(sqa.Integer, autoincrement=True, primary_key=True)
    titulo: str = sqa.Column(sqa.String(45), nullable=False)
    url_fonte: str = sqa.Column(sqa.String(256))
    descricao: str = sqa.Column(sqa.String(256))
    usuario_id: int = sqa.Column(sqa.Integer, sqa.ForeignKey('usuarios.id'))
    criador = orm.relationship('UsuarioModel',  back_populates='artigos', lazy='joined')