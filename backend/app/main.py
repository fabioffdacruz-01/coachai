from fastapi import FastAPI

app = FastAPI(
    title="CoachAI",
    description="API da plataforma CoachAI",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Bem-vindo ao CoachAI!"
    }