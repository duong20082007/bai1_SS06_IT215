from fastapi import FastAPI

app = FastAPI()

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    },
    {
        "id": 3,
        "code": "DB101",
        "name": "Database Design",
        "level": "intermediate",
        "price": 1800000
    }
]

@app.get("/health")
def health_check():
    return {"message": "API is running"}

@app.get("/courses")
def get_all_courses():
    return courses

@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    if course_id <= 0:
        return {
            "status": 400, 
            "message": "Mã khóa học không hợp lệ. Phải lớn hơn 0."
        }
    
    for course in courses:
        if course["id"] == course_id:
            return course  

    return {
        "status": 404, 
        "message": "Không tìm thấy khóa học"
    }