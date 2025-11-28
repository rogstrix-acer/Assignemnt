from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class MemberCreate(BaseModel):
    name: str
    phone: str

class MemberResponse(BaseModel):
    id: int
    name: str
    phone: str
    join_date: datetime
    status: str
    total_check_ins: int

class PlanCreate(BaseModel):
    name: str
    price: float
    duration_days: int

class PlanResponse(BaseModel):
    id: int
    name: str
    price: float
    duration_days: int

class SubscriptionCreate(BaseModel):
    member_id: int
    plan_id: int
    start_date: datetime

class SubscriptionResponse(BaseModel):
    id: int
    member_id: int
    plan_id: int
    start_date: datetime
    end_date: datetime

class AttendanceCreate(BaseModel):
    member_id: int

class AttendanceResponse(BaseModel):
    id: int
    member_id: int
    check_in_time: datetime

class CurrentSubscriptionResponse(BaseModel):
    subscription: Optional[SubscriptionResponse] = None
    message: Optional[str] = None

class AttendanceListResponse(BaseModel):
    attendance_records: List[AttendanceResponse]