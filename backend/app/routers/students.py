from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class StudentCreate(BaseModel):
    nome: str
    idade: int
    objetivo: str


students = [
    {
        "id": 1,
        "nome": "Fábio Cruz",
        "idade": 45,
        "objetivo": "Hipertrofia",
    },
    {
        "id": 2,
        "nome": "Maria",
        "idade": 32,
        "objetivo": "Emagrecimento",
    },
]


@router.get("/students")
def list_students():
    return students


@router.post("/students", status_code=201)
def create_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        **student.model_dump(),
    }

    students.append(new_student)

    return new_student
