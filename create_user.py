from models.usuarios import Usuario
from database import SessionLocal
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

senha_criptografada = bcrypt_context.hash("123")
novo_usuario = Usuario(nome='bagas', senha=senha_criptografada, loja='CZ', cargo='Mega Brain')

session = SessionLocal()
session.add(novo_usuario)
session.commit()
session.close()