from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from report_routes import report_router
from auth_routes import auth_router

app.include_router(report_router)
app.include_router(auth_router)