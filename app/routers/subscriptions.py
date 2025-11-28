from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Subscription)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(database.get_db)):
    member = db.query(models.Member).filter(models.Member.id == subscription.member_id).first()
    plan = db.query(models.Plan).filter(models.Plan.id == subscription.plan_id).first()
    
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    end_date = subscription.start_date + timedelta(days=plan.duration_days)
    new_subscription = models.Subscription(
        member_id=subscription.member_id,
        plan_id=subscription.plan_id,
        start_date=subscription.start_date,
        end_date=end_date
    )
    
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    
    return new_subscription

@router.get("/members/{member_id}/current", response_model=schemas.Subscription)
def get_current_subscription(member_id: int, db: Session = Depends(database.get_db)):
    today = datetime.utcnow()
    subscription = db.query(models.Subscription).filter(
        models.Subscription.member_id == member_id,
        models.Subscription.start_date <= today,
        models.Subscription.end_date >= today
    ).first()
    
    if not subscription:
        raise HTTPException(status_code=404, detail="No active subscription found for this member")
    
    return subscription