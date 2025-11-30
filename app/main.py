from fastapi import FastAPI
from app.database import engine
from app.routers import members, plans, subscriptions, attendance
from app.models import Base

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(members.router)
app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
app.include_router(attendance.router)