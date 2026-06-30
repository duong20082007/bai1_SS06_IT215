from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

students = [
    {
        "full_name": "Nguyen Van A",
        "email": "vana@gmail.com",
        "age": 20,
        "course": "python",
        "phone": "0987654321"
    }
]

class CreateStudents(BaseModel):
    full_name: str = Field(pattern=r'^[a-zA-Z\s]+$', min_length=3)
    email: str = Field(pattern=r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
    age: int
    course: str
    phone: str
    
@app.post('/students')
def register_student(request_data: StudentPayload):
    for std in student_records:
        if request_data.email == std.get('email'): 
            return {
                "detail": "Email đã tồn tại trong hệ thống"
            }
            
    new_std = {
        'full_name': request_data.full_name,
        'email': request_data.email,
        'age': request_data.age,
        'course': request_data.course,
        'phone': request_data.phone,
    }
    
    student_records.append(new_std)
    
    return {
        'message': 'Đã thêm sinh viên thành công'
    }