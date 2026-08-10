from fastapi import APIRouter, HTTPException, Depends
from main_fastapi import bcrypt_context, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from models.usuarios import Usuario
from database import pegar_sessao
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

def criar_token(id_usuario, ducarao_token = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + ducarao_token
    dic_info = {"sub": id_usuario, "exp": data_expiracao}
    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_codificado

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
        refresh_token = criar_token(usuario.id, ducarao_token=timedelta(days=7))
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }