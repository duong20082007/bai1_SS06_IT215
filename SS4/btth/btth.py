from fastapi import FastAPI

app = FastAPI()

courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online"
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline"
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online"
    }
]

@app.get("/courses")
def get_all_courses():
    return {
        "message": "Lấy danh sách khóa học thành công",
        "data": courses
    }

@app.get("/courses/search")
def search_courses(mode: str = None, category: str = None):
    result = []
    
    for course in courses:
        is_valid = True
        
        if mode is not None:
            if course.get("mode") != mode:
                is_valid = False
                
        if category is not None:
            if course.get("category") != category:
                is_valid = False
                
        if is_valid == True:
            result.append(course)
            
    return {
        "message": "Lọc khóa học thành công",
        "data": result
    }

@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    for course in courses:
        if course.get("id") == course_id:
            return {
                "message": "Tìm thấy khóa học",
                "data": course
            }
            
    return {
        "message": "Không tìm thấy khóa học"
    }