from sqlalchemy import Column, NVARCHAR, Integer, Boolean
from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", NVARCHAR, nullable=False)
    senha = Column("senha", NVARCHAR, nullable=False)
    cargo = Column("cargo", NVARCHAR, default=None)
    loja = Column("loja", NVARCHAR)
    admin = Column("admin", Boolean, default=False)
    

    def __init__(self, nome, senha, loja, cargo=None, admin=False):
        self.nome = nome
        self.senha = senha
        self.cargo = cargo
        self.loja = loja
        self.admin = admin
        

