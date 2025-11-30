from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/members", response_model=schemas.MemberResponse)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    db_member = models.Member(name=member.name, phone=member.phone)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

@router.get("/members", response_model=list[schemas.MemberResponse])
def list_members(status: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Member)
    if status:
        query = query.filter(models.Member.status == status)
    members = query.all()
    return members