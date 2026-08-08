from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


db = create_engine("sqlite:///raw_data.db")

SessionLocal = sessionmaker(
    bind=db,
    autoflush=False,
    autocommit=False
)

def pegar_sessao():
    try:
        Session = SessionLocal
        session = Session()
        yield session
    finally:
        session.close()

Base = declarative_base()