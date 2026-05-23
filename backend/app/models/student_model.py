from sqlalchemy import Column, Interger, String, TIMESTAMP
from app.database import Base
from sqlalchemy.sql import func


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(20), unique=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    password = Column(String(255), nullable=False)
    department = Column(String(50))
    year = Column(Integer)
    section = Column(String(10))
    phone = Column(String(15))
    parent_phone = Column(String(15))
    face_image = Column(String(255))
    device_id = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())