from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["GET", "POST"], 
    allow_headers=["*"],
)

@app.get("/login.html", response_class=FileResponse)
async def pagina_login():
    return "templates/login.html"

@app.get("/index.html", response_class=FileResponse)
async def pagina_principal():
    return "templates/index.html"


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login_form")

from report_routes import report_router
from auth_routes import auth_router

app.include_router(report_router)
app.include_router(auth_router)