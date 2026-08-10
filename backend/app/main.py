from fastapi import FastAPI
from app.routers import students
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