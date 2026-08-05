from fastapi import APIRouter

report_router = APIRouter(prefix="/report", tags=["Report"])

@report_router.get("/consulta_estoque")
async def consultar_estoque():

    return {"mensagem": "Relatório gerado"}

@report_router.get("/pedido_semanal")
async def pedido_semanal():

    return {"mensagem": "Relatório gerado"}

@report_router.get("/ruptura_total")
async def ruptura_total():

    return {"mensagem": "Relatório gerado"}