from models.usuarios import Usuario
from database import SessionLocal
from passlib.context import CryptContext
from main_fastapi import bcrypt_context

senha_criptografada = bcrypt_context.hash("123")
novo_usuario = Usuario(nome='vigas', senha=senha_criptografada, loja='CZ', cargo='cop tief')

session = SessionLocal()
session.add(novo_usuario)
session.commit()
session.close()