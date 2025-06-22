from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..models import WheatProductionData
from ..schemas import WheatProductionDataOut
from ..utils.filters import apply_filters

router = APIRouter()

@router.get("/dashboard/production", response_model=List[WheatProductionDataOut])
def get_production_data(
    start_date: date = Query(None),
    end_date: date = Query(None),
    types: List[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(WheatProductionData)
    query = apply_filters(query, start_date, end_date, types)
    return query.all()
