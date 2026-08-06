import pandas as pd
from models.consulta_estoque_bot import ConsultaEstoqueBOT
from models.consulta_estoque_qdb import ConsultaEstoqueQDB
from models.consulta_estoque_eud import ConsultaEstoqueEUD
from models.ruptura_total_bot import RupturaTotalBot
from models.pedido_semanal_especial import PedidoSemanalEspecial
from database import SessionLocal

consulta_estoque_eud = pd.read_excel(r'raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx', sheet_name='EUD')
consulta_estoque_bot = pd.read_excel(r"raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx", sheet_name='BOT')
consulta_estoque_qdb = pd.read_excel(r"raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx", sheet_name='QDB')
pedidos_semanais = pd.read_excel(r"raw_data\Pedidos Semanais Especiais - BOT - 202612.xlsx")
ruptura_total = pd.read_excel(r"raw_data\RUPTURA-TOTAL_BOT_10286_202611_20260729144750.xlsx")

def padronizar_coluna(df):
    substituir = str.maketrans({
        'ã': 'a',
        'ç': 'c',
        'ó': 'o',
        'á': 'a'
    })

    df.columns = [coluna.translate(substituir).lower() for coluna in df.columns]
    df.columns = [coluna.replace(' ','_').replace('_+','').replace('_(r$)','').replace('_(%)','') for coluna in df.columns]

    return df

padronizar_coluna(consulta_estoque_eud)
padronizar_coluna(consulta_estoque_bot)
padronizar_coluna(consulta_estoque_qdb)
padronizar_coluna(pedidos_semanais)
padronizar_coluna(ruptura_total)

def enviar_dados(df, classe_tabela):
    dados = df.to_dict("records")
    session = SessionLocal()
    try:
        session.bulk_insert_mappings(classe_tabela, dados)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

enviar_dados(consulta_estoque_eud, ConsultaEstoqueEUD)
enviar_dados(consulta_estoque_bot, ConsultaEstoqueBOT)
enviar_dados(consulta_estoque_qdb, ConsultaEstoqueQDB)
enviar_dados(pedidos_semanais, PedidoSemanalEspecial)
enviar_dados(ruptura_total, RupturaTotalBot)