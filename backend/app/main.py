from fastapi import FastAPI
from app.routes import auth

from app.routes import attendance

app = FastAPI()

app.include_router(auth.router)
app.include_router(attendance.router)