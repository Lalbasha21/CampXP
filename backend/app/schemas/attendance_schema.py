from pydantic import BaseModel

class AttendanceSessionCreate(BaseModel):
    faculty_id: int
    subject_id: int
class AttendanceMarkRequest(BaseModel):
    student_id: int
    qr_token: str