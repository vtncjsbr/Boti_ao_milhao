from sqlalchemy import Column, String, Integer, Float
from database import Base


class ConsultaEstoqueBOT(Base):
    __tablename__ = "raw_consulta_de_estoque_bot"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    sku = Column("SKU", Integer)
    sku_para = Column("SKU PARA", String)
    descricao = Column("DESCRICAO", String)
    categoria = Column("CATEGORIA", String)
    classe = Column("CLASSE", String)
    fases_produto = Column("FASES PRODUTO", String)
    lancamento = Column("LANCAMENTO", String)
    desativacao = Column("DESATIVACAO", String)
    pdv = Column("PDV", Integer)
    estoque_atual = Column("ESTOQUE ATUAL", Integer)
    estoque_em_transito = Column("ESTOQUE EM TRANSITO", Integer)
    pedido_pendente = Column("PEDIDO PENDENTE", Integer)
    cobertura_alvo = Column("COBERTURA ALVO", Integer)
    estoque_de_seguranca = Column("ESTOQUE DE SEGURANCA", Integer)
    ddv_previsto = Column("DDV PREVISTO", Float)
    cobertura_atual = Column("COBERTURA ATUAL", Integer)
    cobertura_atual_transito = Column("COBERTURA ATUAL + TRANSITO", Integer)
    cobertura_projetada = Column("COBERTURA PROJETADA", Integer)

