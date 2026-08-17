from sqlalchemy import Column, NVARCHAR, Integer, Date
from database import Base


class RelatorioAbcVendas(Base):
    __tablename__ = "raw_relatorio_abc_vendas"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quebra = Column('QUEBRA', NVARCHAR)
    quebra2 = Column('QUEBRA2', NVARCHAR)
    codigo = Column('CODIGO', Integer)
    descricao = Column('DESCRICAO', NVARCHAR)
    quantidade = Column('QUANTIDADE', Integer)
    faturamento = Column('FATURAMENTO', NVARCHAR)
    preco_medio = Column('PRECO MEDIO', NVARCHAR)
    custo_total = Column('CUSTO TOTAL', NVARCHAR)
    imposto_estadual = Column('IMPOSTO ESTADUAL', NVARCHAR)
    imposto_federal = Column('IMPOSTO FEDERAL', NVARCHAR)
    lucro = Column('LUCRO', NVARCHAR)
    margem = Column('MARGEM', NVARCHAR)
    markup = Column('MARKUP', NVARCHAR)
    participacao = Column('PARTICIPACAO', NVARCHAR)
    acumulado = Column('ACUMULADO', NVARCHAR)
    classificacao = Column('CLASSIFICACAO', NVARCHAR, nullable=True)
    icms_st = Column('ICMS ST', NVARCHAR, nullable=True)
    fecop_st = Column('DECOP ST', NVARCHAR, nullable=True)