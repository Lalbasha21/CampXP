from sqlalchemy.orm import Session
from app.models.student_model import Student
from app.schemas.auth_schema import StudentRegister
from app.utils.helpers import hash_password
from app.schemas.auth_schema import LoginRequest
from app.utils.helpers import verify_password
from app.utils.jwt_handler import create_access_token

def register_student(db: Session, student: StudentRegister):

    hashed_pw = hash_password(student.password)

    new_student  = Student(
        student_id=student.student_id,
        full_name=student.full_name,
        email=student.email,
        password=hashed_pw,
        department=student.department,
        year=student.year,
        section=student.section,
        phone=student.phone,
        parent_phone=student.parent_phone
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def login_student(db: Session, login_data: LoginRequest):

    student = db.query(Student).filter(
        Student.email == login_data.email
    ).first()

    if not student:
        return {
            "error": "Invalid email"
        }

    valid_password = verify_password(
        login_data.password,
        student.password
    )

    if not valid_password:
        return {
            "error": "Invalid password"
        }

    token = create_access_token({
        "student_id": student.id,
        "email": student.email
    })

    return {
        "message": "Login successful",
        "access_token": token,
        "student": {
            "id": student.id,
            "name": student.full_name,
            "email": student.email
        }
    }