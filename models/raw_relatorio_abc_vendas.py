from sqlalchemy import Column, String, Integer, Date
from database import Base


class RelatorioAbcVendas(Base):
    __tablename__ = "raw_relatorio_abc_vendas"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quebra = Column('QUEBRA', String)
    quebra2 = Column('QUEBRA2', String)
    codigo = Column('CODIGO', Integer)
    descricao = Column('DESCRICAO', String)
    quantidade = Column('QUANTIDADE', Integer)
    faturamento = Column('FATURAMENTO', String)
    preco_medio = Column('PRECO MEDIO', String)
    custo_total = Column('CUSTO TOTAL', String)
    imposto_estadual = Column('IMPOSTO ESTADUAL', String)
    imposto_federal = Column('IMPOSTO FEDERAL', String)
    lucro = Column('LUCRO', String)
    margem = Column('MARGEM', String)
    markup = Column('MARKUP', String)
    participacao = Column('PARTICIPACAO', String)
    acumulado = Column('ACUMULADO', String)
    classificacao = Column('CLASSIFICACAO', String, nullable=True)
    icms_st = Column('ICMS ST', String, nullable=True)
    fecop_st = Column('DECOP ST', String, nullable=True)