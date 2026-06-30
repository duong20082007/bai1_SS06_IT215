from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

student_records = [
    {"id": 1, "name": "Nguyen Van A"},
    {"id": 2, "name": "Tran Thi B"},
    {"id": 3, "name": "Le Van C"}
]

course_records = [
    {"id": 1, "name": "FastAPI Basic", "capacity": 2},
    {"id": 2, "name": "Python OOP", "capacity": 2}
]

registration_records = [
    {"id": 1, "student_id": 1, "course_id": 1},
    {"id": 2, "student_id": 2, "course_id": 1}
]

class RegistrationPayload(BaseModel):
    student_id: int
    course_id: int

@app.post("/registrations")
def create_registration(registration_id: int, request_data: RegistrationPayload):

    target_course = None
    for course in course_records:
        if course["id"] == request_data.course_id:
            target_course = course
            break
            
    if not target_course:
        return {
            "message": "Khóa học không tồn tại",
            "data": None
        }

    student_exists = False
    for student in student_records:
        if student["id"] == request_data.student_id:
            student_exists = True
            break
            
    if not student_exists:
        return {
            "message": "Học viên không tồn tại",
            "data": None
        }

    current_enrollments = 0
    for reg in registration_records:
        if reg["course_id"] == request_data.course_id:
            current_enrollments += 1
            if reg["student_id"] == request_data.student_id:
                return {
                    "message": "Học viên đã đăng ký khóa học này",
                    "data": None
                }

    if current_enrollments >= target_course["capacity"]:
        return {
            "message": "Khóa học đã đầy",
            "data": None
        }

    new_registration = {
        "id": registration_id,
        "student_id": request_data.student_id,
        "course_id": request_data.course_id
    }
    
    registration_records.append(new_registration)
    
    return {
        "message": "Đăng ký thành công",
        "data": new_registration
    }