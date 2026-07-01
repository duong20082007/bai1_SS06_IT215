from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

courses = [
    {"id": 1, "code": "PY101", "name": "Python Basic", "duration": 30, "fee": 3000000},
    {"id": 2, "code": "API101", "name": "FastAPI Basic", "duration": 24, "fee": 2500000},
    {"id": 3, "code": "JV101", "name": "Java Basic", "duration": 40, "fee": 4000000}
]

class CoursePayload(BaseModel):
    code: str
    name: str
    duration: int
    fee: float

@app.post('/courses')
def create_course(course_id: int, new_course: CoursePayload):
    course_data = {
        'id': course_id,
        'code': new_course.code,
        'name': new_course.name,
        'duration': new_course.duration,
        'fee': new_course.fee
    }
    courses.append(course_data)
    
    return {
        'message': 'Thêm khóa học thành công',
        'data': course_data
    }

@app.get('/courses')
def get_courses(keyword: str = None, min_fee: float = None, max_fee: float = None):
    filter_courses = []
    
    for course in courses:
        if keyword:
            kw = keyword.lower()
            if kw not in course['name'].lower() and kw not in course['code'].lower():
                continue
                
        if min_fee is not None and course['fee'] < min_fee:
            continue
            
        if max_fee is not None and course['fee'] > max_fee:
            continue
            
        filter_courses.append(course)
        
    if filter_courses:
        return {
            'message': 'Lấy danh sách khóa học thành công',
            'data': filter_courses
        }
        
    return {
        'message': 'Không tìm thấy khóa học phù hợp',
        'data': None
    }

@app.get('/courses/{course_id}')
def get_course_by_id(course_id: int):
    for course in courses:
        if course['id'] == course_id:
            return {
                'message': 'Tìm thấy khóa học',
                'data': course
            }
            
    return {
        'message': 'Khóa học không tồn tại',
        'data': None
    }

@app.put('/courses/{course_id}')
def update_course(course_id: int, update_data: CoursePayload):
    for course in courses:
        if course['id'] == course_id:
            course['code'] = update_data.code
            course['name'] = update_data.name
            course['duration'] = update_data.duration
            course['fee'] = update_data.fee
            
            return {
                'message': 'Cập nhật khóa học thành công',
                'data': course
            }
            
    return {
        'message': 'Khóa học không tồn tại',
        'data': None
    }

@app.delete('/courses/{course_id}')
def delete_course(course_id: int):
    for course in courses:
        if course['id'] == course_id:
            courses.remove(course)
            return {
                'message': 'Xóa khóa học thành công',
                'data': course
            }
            
    return {
        'message': 'Khóa học không tồn tại',
        'data': None
    }
