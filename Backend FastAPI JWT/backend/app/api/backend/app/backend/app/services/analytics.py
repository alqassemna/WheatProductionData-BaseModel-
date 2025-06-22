import numpy as np

def simulate_yield_scenario(base_yield, temp_delta, drought_severity, price_change):
    # Example: simple regression coefficients
    yield_sensitivity_temp = -0.05  # yield decrease per °C
    yield_sensitivity_drought = -0.2  # yield decrease per drought index
    price_sensitivity = 0.1  # yield increase per price %

    projected = (base_yield +
                 yield_sensitivity_temp * temp_delta +
                 yield_sensitivity_drought * drought_severity +
                 price_sensitivity * price_change)
    return round(max(projected, 0), 2)

# Example scenario API endpoint
from fastapi import APIRouter, Query
from ..services.analytics import simulate_yield_scenario

router = APIRouter()

@router.get("/analytics/scenario")
def scenario(
    base_yield: float = Query(...),
    temp_delta: float = Query(...),
    drought_severity: float = Query(...),
    price_change: float = Query(...)):
    return {"projected_yield": simulate_yield_scenario(base_yield, temp_delta, drought_severity, price_change)}
