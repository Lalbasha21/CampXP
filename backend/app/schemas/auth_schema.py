from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class StudentRegister(BaseModel):
    student_id: str
    full_name: str
    email: EmailStr
    password: str
    department: str
    year: int
    section: str
    phone: str
    parent_phone: str
