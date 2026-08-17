from sqlalchemy import Column, NVARCHAR, Integer, Float
from database import Base


class RupturaTotalBot(Base):
    __tablename__ = "raw_ruptura_total_bot"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ciclo = Column("CICLO", Integer)
    ponto_de_venda = Column("PONTO DE VENDA", Integer)
    canal = Column("CANAL", NVARCHAR)
    sku = Column("SKU", Integer)
    descricao = Column("DESCRICAO", NVARCHAR)
    categoria = Column("CATEGORIA", NVARCHAR)
    marca = Column("MARCA", NVARCHAR)
    classe = Column("CLASSE", NVARCHAR)
    valor_da_receita = Column("VALOR DA RECEITA", Float)
    valor_da_ruptura = Column("VALOR DA RUPTURA", Float)
    percentual_da_ruptura = Column("PERCENTUAL DA RUPTURA", Float)
    quantidade_de_ruptura = Column("QUANTIDADE DE RUPTURA", Float)
    macro_causa = Column("MACRO CAUSA", NVARCHAR)
    origem_ruptura = Column("ORIGEM RUPTURA", NVARCHAR)