from fastapi import APIRouter
from app.api.v1.endpoints import seizures, lifestyles, reports

api_router = APIRouter()
api_router.include_router(seizures.router, prefix="/seizures", tags=["seizures"])
api_router.include_router(lifestyles.router, prefix="/lifestyles", tags=["lifestyles"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
