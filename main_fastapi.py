from fastapi import FastAPI

app = FastAPI()

from report_routes import report_router

app.include_router(report_router)