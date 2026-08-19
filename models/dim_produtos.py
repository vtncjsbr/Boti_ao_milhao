from sqlalchemy import Column, Integer, NVARCHAR
from database import Base


class DimProdutos(Base):
    __tablename__ = "dim_produtos"

    id = Column("ID", Integer, primary_key=True)
    sku = Column("SKU", Integer)
    descricao = Column("DESCRICAO", NVARCHAR)
    loja = Column("LOJA", NVARCHAR)
    categoria = Column("CATEGORIA", NVARCHAR)
    subcategoria = Column("SUBCATEGORIA", NVARCHAR)

"""
Index: 10918 entries, 0 to 10918
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   SKU           10854 non-null  object
 1   DESCRICAO     10918 non-null  object
 2   LOJA          9960 non-null   str   
 3   CATEGORIA     9960 non-null   str   
 4   SUBCATEGORIA  1463 non-null   str
"""