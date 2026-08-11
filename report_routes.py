from fastapi import APIRouter, Depends
from dependencies import pegar_sessao, verificar_token
from models.raw_relatorio_abc_vendas import RelatorioAbcVendas
from database import db
from sqlalchemy import select
import pandas as pd
from io import BytesIO
from fastapi.responses import StreamingResponse

report_router = APIRouter(prefix="/report", tags=["Report"], dependencies=[Depends(verificar_token)])

@report_router.get("/vendas")
async def relatorio_vendas():
    stmt = select(RelatorioAbcVendas)

    with db.connect() as conn:
        df = pd.read_sql(stmt, con=conn)

    arquivo = BytesIO()

    with pd.ExcelWriter(arquivo) as writer:
        df.to_excel(writer, index=False, sheet_name="Vendas")
    arquivo.seek(0)

    return StreamingResponse(arquivo, 
                            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                            headers={"Content-Disposition": "attachment; filename=relatorio_vendas.xlsx"
            })