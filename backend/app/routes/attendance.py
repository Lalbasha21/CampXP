from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.attendance_schema import AttendanceSessionCreate
from app.services.attendance_service import create_attendance_session

router = APIRouter(prefix="/attendance")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/start")
def start_attendance(
    data: AttendanceSessionCreate,
    db: Session = Depends(get_db)
):
    return create_attendance_session(db, data)  

