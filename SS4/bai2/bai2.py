# Có, endpoint hiện tại có sử dụng Path Parameter.

# Path Parameter chính là {status}.

# Biến status sẽ nhận giá trị là chuỗi "pending".

# Vì hàm xử lý nhận được giá trị status từ URL nhưng lại không sử dụng nó để lọc danh sách. 
# API đang trả về toàn bộ mảng orders gốc bất kể người dùng truyền vào trạng thái nào.

# Đó là dòng: return orders.

# Sua 
from fastapi import FastAPI

app = FastAPI()

orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]

@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    valid_statuses = ["pending", "paid", "cancelled"]
    
    if status not in valid_statuses:
        return {"message": "Trạng thái đơn hàng không hợp lệ"}
        
    filtered_orders = []
    
    for order in orders:
        if order.get("status") == status:
            filtered_orders.append(order)
            
    return filtered_orders