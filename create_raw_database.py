from database import Base, db

from models.consulta_estoque_bot import ConsultaEstoqueBOT
from models.consulta_estoque_eud import ConsultaEstoqueEUD
from models.consulta_estoque_qdb import ConsultaEstoqueQDB
from models.pedido_semanal_especial import PedidoSemanalEspecial
from models.ruptura_total_bot import RupturaTotalBot

Base.metadata.create_all(bind=db)