from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.auth_schema import StudentRegister
from app.services.auth_service import register_student

from app.schemas.auth_schema import LoginRequest
from app.services.auth_service import login_student

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(
    student: StudentRegister,
    db: Session = Depends(get_db)
):
    return register_student(db, student)


@router.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    return login_student(db, login_data)
