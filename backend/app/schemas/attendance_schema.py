from pydantic import BaseModel

class AttendanceSessionCreate(BaseModel):
    faculty_id: int
    subject_id: int
