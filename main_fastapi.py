from fastapi import FastAPI
from passlib.context import CryptContext

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from report_routes import report_router
from auth_routes import auth_router

app.include_router(report_router)
app.include_router(auth_router)