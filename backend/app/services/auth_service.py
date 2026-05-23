from sqlalchemy.orm import Session
from app.modules.student_model import Student
from app.schemas.auth_schema import StudentRegister
from app.utils.helpers import hash_password


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