from fastapi import APIRouter, HTTPException, Depends
from main_fastapi import bcrypt_context
from models.usuarios import Usuario
from database import pegar_sessao

def criar_token(id_usuario):
    token = f"aosmdasdmidmow{id_usuario}"
    return token

def autenticar_usuario(nome, senha, session):
    usuario = session.query(Usuario).filter(Usuario.nome==nome).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
async def login(nome, senha, session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(nome, senha, session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais inválidas")
    else:
        access_token = criar_token(usuario.id)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }