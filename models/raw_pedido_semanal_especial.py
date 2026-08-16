from sqlalchemy import Column, String, Integer, Float
from database import Base


class PedidoSemanalEspecial(Base):
    __tablename__ = "raw_pedidos_semanais_especiais"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ciclo = Column("CICLO", Integer)
    regiao = Column("REGIAO", String)
    canal = Column("CANAL", String)
    codigo = Column("CODIGO", Integer)
    descricao = Column("DESCRICAO", String)
    iaf = Column("IAF", String)
    tipo_de_pedido = Column("TIPO DE PEDIDO", String)
    foco = Column("FOCO", String)
    unidade_de_negocio = Column("UNIDADE DE NEGOCIO", String)
    marca = Column("MARCA", String)
    categoria = Column("CATEGORIA", String)
    subcategoria = Column("SUBCATEGORIA", String)
    quantidade_por_caixa = Column("QUANTIDADE POR CAIXA", Integer)
    tipo_de_promocao = Column("TIPO DE PROMOCAO", String)
    catalogo = Column("CATALOGO", String)
    tipo_de_produto = Column("TIPO DE PRODUTO", String)
    acao_consumidor = Column("ACAO CONSUMIDOR", String)
    percentual_de_desconto_consumidor = Column("PERCENTUAL DE DESCONTO CONSUMIDOR", String)
    acao_revendedor = Column("ACAO REVENDEDOR", String)
    percentual_de_desconto_revendedor = Column("PERCENTUAL DE DESCONTO REVENDEDOR", String)
    sortimento_p = Column("SORTIMENTO P", String)
    sortimento_m = Column("SORTIMENTO M", String)
    sortimento_g = Column("SORTIMENTO G", String)