from pydantic import BaseModel

class WorkoutCreate(BaseModel):
    nome: str
    objetivo: str
    student_id: int

class WorkoutResponse(WorkoutCreate):
    id: int

    class Config:
        from_attributes = True