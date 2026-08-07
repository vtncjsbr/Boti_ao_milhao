from database import Base, db

from models.consulta_estoque_bot import ConsultaEstoqueBOT
from models.consulta_estoque_eud import ConsultaEstoqueEUD
from models.consulta_estoque_qdb import ConsultaEstoqueQDB
from models.pedido_semanal_especial import PedidoSemanalEspecial
from models.ruptura_total_bot import RupturaTotalBot
from models.usuarios import Usuario
from models.raw_relatorio_abc_vendas import RelatorioAbcVendas

Base.metadata.create_all(bind=db)