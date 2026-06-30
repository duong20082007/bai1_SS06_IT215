from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class GetStudent(BaseModel):
    id: int
    name: str = Field(min_length=1)
    age: int = Field(gt=18)

@app.get('/students')
def get_root():
    return {
        'data': students
    }

@app.get('/student')
def get_student(student: GetStudent):
    return {
        'data': student
    }