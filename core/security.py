from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correto, comparando a senha em texto puro, informada pelo o usuário e o hash das senha que estará salvo no banco de dados.
    """

    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
    Função pega a senha em formato de texto puro e transforma(cripotografa) a senha informada pelo o usuário.
    """

    return CRIPTO.hash(senha)