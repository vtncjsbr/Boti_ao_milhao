from fastapi import FastAPI, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
API_BASE_URL = os.getenv("API_BASE_URL", "")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["GET", "POST"], 
    allow_headers=["*"],
)

@app.get("/login.html")
async def pagina_login(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"api_base_url": API_BASE_URL},
    )

@app.get("/index.html")
async def pagina_principal(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"api_base_url": API_BASE_URL},
    )


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login_form")

from report_routes import report_router
from auth_routes import auth_router

app.include_router(report_router)
app.include_router(auth_router)