from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database.connection import SessionLocal
from app.models.student import Student
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@router.post("/students", status_code=201)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(
        nome=student.nome,
        idade=student.idade,
        objetivo=student.objetivo
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return student

@router.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    student_data = db.query(Student).filter(Student.id == student_id).first()

    if student_data is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    student_data.nome = student.nome
    student_data.idade = student.idade
    student_data.objetivo = student.objetivo

    db.commit()
    db.refresh(student_data)

    return student_data

@router.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student_data = db.query(Student).filter(Student.id == student_id).first()

    if student_data is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    db.delete(student_data)
    db.commit()

    return {
        "mensagem": "Aluno removido com sucesso!"
    }
    