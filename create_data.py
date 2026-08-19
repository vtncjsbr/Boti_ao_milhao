import pandas as pd
import numpy as np


def planilha_consulta_estoque(caminho_df: str, sheet_name: str, loja: str):
    df_raw = pd.read_excel(rf'{caminho_df}', sheet_name=sheet_name)
    df_raw = df_raw[['DESCRICAO','CATEGORIA','SKU','SKU_PARA']].drop_duplicates(subset=['DESCRICAO'], ignore_index=True)
    df_raw = df_raw[df_raw['DESCRICAO'].apply(lambda x: isinstance(x, str))]
    df_raw = df_raw.sort_values(by='DESCRICAO', ascending=True)
    df_raw['ID'] = range(1, len(df_raw) + 1)
    df_raw['ID'] = df_raw.index

    df = pd.DataFrame(columns=['ID','SKU','DESCRICAO','CATEGORIA','LOJA'])
    df['DESCRICAO'] = df_raw['DESCRICAO']
    df['SKU'] = np.where(df_raw['SKU_PARA'] == '-', df_raw['SKU'], df_raw['SKU_PARA'])
    df = df.sort_values(by='DESCRICAO', ascending=True)
    df['ID'] = range(1, len(df) + 1)
    df['ID'] = df.index

    df = pd.merge(df, df_raw, on=['DESCRICAO','ID'], how='left')
    df = df.drop(columns=['CATEGORIA_x','SKU_PARA','SKU_y','ID']).rename(columns={'SKU_x':'SKU', 'CATEGORIA_y':'CATEGORIA'})
    df['LOJA'] = loja

    return df
estoque_bot = planilha_consulta_estoque('raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx', 'BOT', 'BOT')
estoque_eud = planilha_consulta_estoque('raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx', 'EUD', 'EUD')
estoque_qdb = planilha_consulta_estoque('raw_data\CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx', 'QDB', 'QDB')

consulta_estoque = pd.concat([estoque_bot,estoque_eud,estoque_qdb])

abc_vendas = pd.read_csv(r"raw_data\relatorioABCVenda (3).csv", encoding='cp1252', sep=';')
abc_vendas = abc_vendas[['Codigo','Descricao']].rename(columns={'Codigo':'SKU','Descricao':'DESCRICAO'})
df = pd.concat([consulta_estoque,abc_vendas])
df = df.drop_duplicates(subset=['DESCRICAO'])

ruptura_bot = pd.read_excel(r"raw_data\RUPTURA-TOTAL_BOT_10286_202611_20260729144750.xlsx")
ruptura_bot = ruptura_bot[['SKU','Descrição','Categoria','Marca']].rename(columns={'Descrição':'DESCRICAO', 'Categoria':"CATEGORIA",'Marca':'LOJA'})
df = pd.concat([df,ruptura_bot])
df = df.drop_duplicates(subset=['DESCRICAO'])

pedidos_semanais = pd.read_excel(r"raw_data\Pedidos Semanais Especiais - BOT - 202612.xlsx")
pedidos_semanais = pedidos_semanais[['Descrição','Subcategoria']].rename(columns={'Descrição': 'DESCRICAO','Subcategoria':'SUBCATEGORIA'})
df = pd.concat([df, pedidos_semanais])
df = df.drop_duplicates(subset=['DESCRICAO'])
df = pd.merge(df, pedidos_semanais, on=['DESCRICAO'], how='left')
df = df.drop(columns=['SUBCATEGORIA_x']).rename(columns={'SUBCATEGORIA_y':'SUBCATEGORIA'})
df = df.drop_duplicates(subset=['DESCRICAO'])