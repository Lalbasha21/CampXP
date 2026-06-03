from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base


class AttendanceSession(Base):
    __tablename__ = "attendance_sessions"

    id = Column(Integer, primary_key=True, index=True)
    faculty_id = Column(Integer, nullable=False)
    subject_id = Column(Integer, nullable=False)
    qr_token = Column(String(255), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(String(20), default="active")
    created_at = Column(TIMESTAMP, server_default=func.now())