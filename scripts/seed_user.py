import os

from dotenv import load_dotenv
from passlib.context import CryptContext

from database import SessionLocal
from models.usuarios import Usuario

load_dotenv()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

DEFAULT_USER = os.getenv("DEFAULT_USER", "vigas")
DEFAULT_PASSWORD = os.getenv("DEFAULT_PASSWORD", "123")
DEFAULT_LOJA = os.getenv("DEFAULT_LOJA", "CZ")
DEFAULT_CARGO = os.getenv("DEFAULT_CARGO", "cop tief")


def seed_user():
    session = SessionLocal()
    try:
        existing = session.query(Usuario).filter(Usuario.nome == DEFAULT_USER).first()
        if existing:
            print(f"User '{DEFAULT_USER}' already exists, skipping seed.")
            return

        session.add(
            Usuario(
                nome=DEFAULT_USER,
                senha=bcrypt_context.hash(DEFAULT_PASSWORD),
                loja=DEFAULT_LOJA,
                cargo=DEFAULT_CARGO,
            )
        )
        session.commit()
        print(f"User '{DEFAULT_USER}' created successfully.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_user()
