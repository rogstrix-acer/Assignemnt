from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Plan
from app.schemas import PlanCreate, PlanResponse
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=PlanResponse)
def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    db_plan = Plan(name=plan.name, price=plan.price, duration_days=plan.duration_days)
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

@router.get("/", response_model=list[PlanResponse])
def get_plans(db: Session = Depends(get_db)):
    plans = db.query(Plan).all()
    return plans