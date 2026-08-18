from fastapi import FastAPI
from app.routers import students
from app.database.connection import Base, engine
from app.models import student, workout
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="CoachAI",
    description="API da plataforma CoachAI",
    version="0.1.0"
)

app.include_router(students.router)


@app.get("/")
def root():
    return {
        "message": "Bem-vindo ao CoachAI!"
    }