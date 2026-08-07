from sqlalchemy import Column, String, Integer, Boolean
from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    cargo = Column("cargo", String, default=None)
    loja = Column("loja", String)
    admin = Column("admin", Boolean, default=False)
    

    def __init__(self, nome, senha, loja, cargo=None, admin=False):
        self.nome = nome
        self.senha = senha
        self.cargo = cargo
        self.loja = loja
        self.admin = admin
        

