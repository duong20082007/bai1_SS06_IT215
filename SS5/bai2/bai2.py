from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

enrollments = [
    {
        "id": 1,
        "student_id": "SV001",
        "course_id": 1
    },
    {
        "id": 2,
        "student_id": "SV002",
        "course_id": 1
    }
]

class CreateEnrollment(BaseModel):
    student_id: str
    course_id: int

@app.post('/enrollment')
def create_enrollment(enrollment_id: int, new_enrollment: CreateEnrollment):
    
    for enrollment in enrollments:
        if enrollment['student_id'] == new_enrollment.student_id and enrollment['course_id'] == new_enrollment.course_id:
            return {
                'message': 'Học viên đã đăng ký khóa học này',
                'data': None
            }
            
    enrollment_data = {
        'id': enrollment_id,
        'student_id': new_enrollment.student_id,
        'course_id': new_enrollment.course_id
    }
    enrollments.append(enrollment_data)
    
    return {
        'message': 'Đăng ký thành công',
        'data': enrollment_data
    }