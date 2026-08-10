from fastapi import APIRouter, HTTPException
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

@router.post("/students")
def create_student(student: StudentCreate):

    new_student = {
        "id": len(students) + 1,
        "nome": student.nome,
        "idade": student.idade,
        "objetivo": student.objetivo
    }

    students.append(new_student)

    return {
        "mensagem": "Aluno cadastrado com sucesso!",
        "aluno": new_student
    }
@router.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Aluno não encontrado"
    )

@router.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):

        for student_data in students:
            if student_data["id"] == student_id:

               student_data["nome"] = student.nome
               student_data["idade"] = student.idade
               student_data["objetivo"] = student.objetivo

               return student_data

            raise HTTPException(
        status_code=404,
        detail="Aluno não encontrado"
    )