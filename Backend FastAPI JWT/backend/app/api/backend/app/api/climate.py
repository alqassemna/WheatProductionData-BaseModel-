from fastapi import APIRouter, Query
from ..services.climate_api import fetch_real_time_climate

router = APIRouter()

@router.get("/climate/real-time")
def get_climate(region: str = Query(...)):
    return fetch_real_time_climate(region)
