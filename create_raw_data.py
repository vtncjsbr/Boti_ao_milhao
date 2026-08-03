import sqlite3
import pandas

conexao = sqlite3.connect('raw_data.db')
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS consulta_de_estoque(
    SKU INT,
    SKU_PARA TEXT,
    DESCRICAO TEXT,
    CATEGORIA TEXT,
    CLASSE TEXT,
    FASES_PRODUTO TEXT,
    LANCAMENTO REAL,
    DESATIVACAO REAL,
    PDV INT,
    ESTOQUE_ATUAL REAL,
    ESTOQUE_EM_TRANSITO INT,
    PEDIDO_PENDENTE INT,
    COBERTURA_ALVO INT,
    ESTOQUE_DE_SEGURANCA INT,
    DDV_PREVISTO REAL,
    COBERTURA_ATUAL INT,
    "COBERTURA_ATUAL + TRANSITO" INT,
    COBERTURA_PROJETADA INT
    )
''')
conexao.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos_semanais_especiais(
    CICLO INT,
    REGIAO TEXT,
    CANAL TEXT,
    CODIGO INT,
    DESCRICAO TEXT,
    IAF TEXT,
    TIPO_DE_PEDIDO TEXT,
    FOCO TEXT,
    UNIDADE_DE_NEGOCIO TEXT,
    MARCA TEXT,
    CATEGORIA TEXT,
    SUBCATEGORIA TEXT,
    QUANTIDADE_POR_CAIXA INT,
    TIPO_DE_PROMOCAO TEXT,
    CATALOGO TEXT,
    TIPO_DE_PRODUTO TEXT,
    ACAO_CONSUMIDOR TEXT,
    PERCEMTUAL_DE_DESCONTO_CONSUMIDOR REAL,
    ACAO_REVENDEDOR TEXT,
    PERCENTUAL_DE_DESCONTO_REVENDEDOR TEXT,
    SORTIMENTO_P TEXT,
    SORTIMENTO_M TEXT,
    SORTIMENTO_G TEXT
    )
''')
conexao.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ruptura_total_bot(
    CICLO INT,
    PONTO_DE_VENDA INT,
    CANAL TEXT,
    SKU INT,
    DESCRICAO TEXT,
    CATEGORIA TEXT,
    MARCA TEXT,
    CLASSE TEXT,
    VALOR_DA_RECEITA REAL,
    VALOR_DA_RUPTURA REAL,
    PERCENTUAL_DE_RUPTURA REAL,
    QUANTIDADE_DE_RUPTURA REAL,
    MACRO_CAUSA TEXT,
    ORIGEM_RUPTURA TEXT
)
''')
conexao.commit()

cursor.close()
conexao.close()

##################################### Alimentar dados no banco #####################################

df_consulta = pandas.read_excel('CONSULTA_DE_ESTOQUE_22247-13948_20260727071046.xlsx')
df_especiais = pandas.read_excel('Pedidos Semanais Especiais - BOT - 202612.xlsx')
df_ruptura = pandas.read_excel('RUPTURA-TOTAL_BOT_10286_202611_20260729144750.xlsx')

conexao = sqlite3.connect('raw_data.db')
df_consulta.to_sql('consulta_de_estoque', conexao, if_exists='replace', index=False)
df_especiais.to_sql('pedidos_semanais_especiais', conexao, if_exists='replace', index=False)
df_ruptura.to_sql('ruptura_total_bot', conexao, if_exists='replace', index=False)
conexao.close()