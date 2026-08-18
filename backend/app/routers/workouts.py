from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.workout import Workout
from app.schemas.workout import WorkoutCreate, WorkoutResponse
router = APIRouter(
    prefix="/workouts",
    tags=["Workouts"]
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=WorkoutResponse)
def create_workout(
    workout: WorkoutCreate,
    db: Session = Depends(get_db)
):
    new_workout = Workout(
        nome=workout.nome,
        objetivo=workout.objetivo,
        student_id=workout.student_id
    )

    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)

    return new_workout