from fastapi import FastAPI

from app.api.router import api_router
from app.api.routes import health
from app.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(health.router)
app.include_router(api_router)
