from fastapi import APIRouter, Depends
from dependencies import pegar_sessao, verificar_token
from models.raw_relatorio_abc_vendas import RelatorioAbcVendas
from models.raw_consulta_estoque_bot import ConsultaEstoqueBOT
from models.dim_produtos import DimProdutos
from database import db
from sqlalchemy import select
import pandas as pd
from io import BytesIO
from fastapi.responses import StreamingResponse

report_router = APIRouter(prefix="/report", tags=["Report"], dependencies=[Depends(verificar_token)])

def criar_relatorio(banco, sheet_name: str, filename: str):
    stmt = select(banco)
    
    with db.connect() as conn:
        df = pd.read_sql(stmt, con=conn)

    arquivo = BytesIO()

    with pd.ExcelWriter(arquivo) as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
    arquivo.seek(0)

    return StreamingResponse(arquivo, 
                            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                            headers={"Content-Disposition": f"attachment; filename={filename}.xlsx"
            })


@report_router.get("/vendas")
async def relatorio_vendas():
    return criar_relatorio(RelatorioAbcVendas, 'vendas', 'vendas')

@report_router.get("/estoque_bot")
async def relatorio_estoque_bot():
    return criar_relatorio(ConsultaEstoqueBOT, 'consulta_estoque_bot', 'consulta_estoque_bot')

@report_router.get("/produtos")
async def relatorio_produtos():
    return criar_relatorio(DimProdutos, 'produtos', 'produtos')