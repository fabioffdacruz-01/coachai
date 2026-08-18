from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.connection import Base

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    objetivo = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)