# from fastapi import FastAPI

# app = FastAPI()
# students = [
#     {"id": 1, "name": "An"},
#     {"id": 2, "name": "Binh"},
#     {"id": 3, "name": "Cuong"},
# ]
# @app.get("/student")
# def get_student():
#     return students[0]

# Endpoint hiện tại: /student.
# Lỗi 404 Not Found: Do máy chủ không tìm thấy đường dẫn. Code định nghĩa /student nhưng lệnh gọi lại là /students.
# Tên /student chưa phù hợp: Theo chuẩn RESTful API, để lấy một tập hợp/danh sách thì phải dùng danh từ số nhiều (/students).
# Lỗi return students[0]: Lệnh này chỉ xuất ra một sinh viên đầu tiên của mảng, sai với yêu cầu lấy toàn bộ danh sách.
# Đường dẫn chuẩn: /students.

# Sửa 
from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"},
]

@app.get("/students")
def get_all_students(): 
    return students