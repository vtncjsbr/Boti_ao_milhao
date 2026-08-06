from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


db = create_engine("sqlite:///raw_data.db")

SessionLocal = sessionmaker(
    bind=db,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()