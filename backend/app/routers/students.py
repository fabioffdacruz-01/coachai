from fastapi import APIRouter

router = APIRouter()

students = [
    {
        "id": 1,
        "nome": "Fábio Cruz",
        "idade": 45,
        "objetivo": "Hipertrofia"
    },
    {
        "id": 2,
        "nome": "Maria",
        "idade": 32,
        "objetivo": "Emagrecimento"
    }
]

@router.get("/students")
def list_students():
    return students