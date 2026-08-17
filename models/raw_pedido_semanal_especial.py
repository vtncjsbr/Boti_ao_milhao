from sqlalchemy import Column, NVARCHAR, Integer, Float
from database import Base


class PedidoSemanalEspecial(Base):
    __tablename__ = "raw_pedidos_semanais_especiais"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ciclo = Column("CICLO", Integer)
    regiao = Column("REGIAO", NVARCHAR)
    canal = Column("CANAL", NVARCHAR)
    codigo = Column("CODIGO", Integer)
    descricao = Column("DESCRICAO", NVARCHAR)
    iaf = Column("IAF", NVARCHAR)
    tipo_de_pedido = Column("TIPO DE PEDIDO", NVARCHAR)
    foco = Column("FOCO", NVARCHAR)
    unidade_de_negocio = Column("UNIDADE DE NEGOCIO", NVARCHAR)
    marca = Column("MARCA", NVARCHAR)
    categoria = Column("CATEGORIA", NVARCHAR)
    subcategoria = Column("SUBCATEGORIA", NVARCHAR)
    quantidade_por_caixa = Column("QUANTIDADE POR CAIXA", Integer)
    tipo_de_promocao = Column("TIPO DE PROMOCAO", NVARCHAR)
    catalogo = Column("CATALOGO", NVARCHAR)
    tipo_de_produto = Column("TIPO DE PRODUTO", NVARCHAR)
    acao_consumidor = Column("ACAO CONSUMIDOR", NVARCHAR)
    percentual_de_desconto_consumidor = Column("PERCENTUAL DE DESCONTO CONSUMIDOR", NVARCHAR)
    acao_revendedor = Column("ACAO REVENDEDOR", NVARCHAR)
    percentual_de_desconto_revendedor = Column("PERCENTUAL DE DESCONTO REVENDEDOR", NVARCHAR)
    sortimento_p = Column("SORTIMENTO P", NVARCHAR)
    sortimento_m = Column("SORTIMENTO M", NVARCHAR)
    sortimento_g = Column("SORTIMENTO G", NVARCHAR)