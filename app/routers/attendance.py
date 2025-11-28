from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Attendance, Member
from app.schemas import AttendanceCreate, AttendanceResponse
from datetime import datetime

router = APIRouter()

@router.post("/attendance/check-in", response_model=AttendanceResponse)
def check_in(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == attendance.member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    
    # Check if the member has an active subscription
    current_subscription = db.query(Subscription).filter(
        Subscription.member_id == member.id,
        Subscription.start_date <= datetime.now(),
        Subscription.end_date >= datetime.now()
    ).first()
    
    if not current_subscription:
        raise HTTPException(status_code=400, detail="No active subscription for this member")
    
    # Create attendance record
    new_attendance = Attendance(member_id=attendance.member_id, check_in_time=datetime.now())
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    
    return new_attendance

@router.get("/members/{member_id}/attendance", response_model=list[AttendanceResponse])
def get_attendance(member_id: int, db: Session = Depends(get_db)):
    attendances = db.query(Attendance).filter(Attendance.member_id == member_id).all()
    if not attendances:
        raise HTTPException(status_code=404, detail="No attendance records found for this member")
    
    return attendances