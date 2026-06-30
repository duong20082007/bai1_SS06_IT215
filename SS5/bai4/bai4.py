from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

product_records = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "stock": 10},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "stock": 5}
]

class ProductUpdatePayload(BaseModel):
    code: str
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

@app.put("/products/{product_id}")
def update_product(product_id: int, request_data: ProductUpdatePayload):
    
    target_product = None
    for product in product_records:
        if product["id"] == product_id:
            target_product = product
            break
            
    if not target_product:
        return {"detail": "Product not found"}
        
    for product in product_records:
        if product["code"] == request_data.code and product["id"] != product_id:
            return {"detail": "Product code already exists"}
            
    target_product["code"] = request_data.code
    target_product["name"] = request_data.name
    target_product["price"] = request_data.price
    target_product["stock"] = request_data.stock
    
    return target_product