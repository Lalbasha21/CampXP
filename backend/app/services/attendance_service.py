import uuid
from app.models.attendance_session_model import AttendanceSession

def create_attendance_session(db, data):

    qr_token = str(uuid.uuid4())

    session = AttendanceSession(
        faculty_id = data.faculty_id,
        subject_id = data.subject_id,
        qr_token = qr_token,
        status = "active"
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "session_id": session.id,
        "qr_token": qr_token
    }

