from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

@app.get('/student/{student_id}')
def get_student(student_id):
    for student in students: 
        if int(student_id) == student['id']:
            return {
                'data' : student
            }
    return {
        'message': 'Không tìm thấy sinh viên',
        'data': None
    }

@app.get('/student')
def get_stduent(age, name):
    return {
        'data' : {
            'age': age,
            'name': name
        }
    }

@app.get('/student/2')
def get_student_2():
    return {
        'message': 'Lấy sinh viên thứ 2',
        'data': {
            'id': 2,
        }
    }


class GetStudent(BaseModel):
    id
    name 
    age 

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