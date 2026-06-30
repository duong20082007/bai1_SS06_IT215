from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products")
def get_products(keyword: str = None, max_price: float = None):
    if max_price is not None and max_price < 0:
        return {
            "detail": "max_price không được âm"
        }

    result = []

    for product in products:
        check_valid = True
        
        if keyword is not None:
            if keyword.lower() not in product["name"].lower():
                check_valid = False
                
        if max_price is not None:
            if product["price"] > max_price:
                check_valid = False
                
        if check_valid == True:
            result.append(product)

    return result