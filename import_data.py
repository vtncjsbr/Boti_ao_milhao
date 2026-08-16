import pandas as pd
from models.raw_consulta_estoque_bot import ConsultaEstoqueBOT
from models.raw_consulta_estoque_qdb import ConsultaEstoqueQDB
from models.raw_consulta_estoque_eud import ConsultaEstoqueEUD
from models.raw_ruptura_total_bot import RupturaTotalBot
from models.raw_pedido_semanal_especial import PedidoSemanalEspecial
from models.raw_relatorio_abc_vendas import RelatorioAbcVendas
from database import SessionLocal

consulta_estoque_eud = pd.read_excel(r'raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx', sheet_name='EUD')
consulta_estoque_bot = pd.read_excel(r"raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx", sheet_name='BOT')
consulta_estoque_qdb = pd.read_excel(r"raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx", sheet_name='QDB')
pedidos_semanais = pd.read_excel(r"raw_data\Pedidos Semanais Especiais - BOT - 202612.xlsx")
ruptura_total = pd.read_excel(r"raw_data\RUPTURA-TOTAL_BOT_10286_202611_20260729144750.xlsx")
relatorio_abc_vendas = pd.read_csv(r'raw_data\relatorioABCVenda (3).csv', encoding='cp1252', sep=';')

def padronizar_coluna(df):
    substituir = str.maketrans({
        'ã': 'a',
        'ç': 'c',
        'ó': 'o',
        'á': 'a',
        'é': 'e'
    })

    df.columns = [coluna.translate(substituir).lower() for coluna in df.columns]
    df.columns = [coluna.replace(' ','_').replace('_+','').replace('_(r$)','').replace('_(%)','') for coluna in df.columns]

    return df

padronizar_coluna(consulta_estoque_eud)
padronizar_coluna(consulta_estoque_bot)
padronizar_coluna(consulta_estoque_qdb)
padronizar_coluna(pedidos_semanais)
padronizar_coluna(ruptura_total)
padronizar_coluna(relatorio_abc_vendas)

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
enviar_dados(relatorio_abc_vendas, RelatorioAbcVendas)