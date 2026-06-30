from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": True
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": False
    },
    {
        "id": 6,
        "title": "FastAPI Basic",
        "author": "Nguyen Van A",
        "category": "web",
        "year": 2023,
        "is_available": True
    }
]

@app.get("/books/statistics")
def get_books_statistics():
    total = len(books)
    
    available_count = 0
    borrowed_count = 0
    
    for book in books:
        if book.get("is_available") == True:
            available_count += 1
        elif book.get("is_available") == False:
            borrowed_count += 1
            
    return {
        "total_books": total,
        "available_books": available_count,
        "borrowed_books": borrowed_count
    }

@app.get("/books/categories")
def get_unique_categories():
    unique_categories = []
    
    for book in books:
        category = book.get("category")
        if category and (category not in unique_categories):
            unique_categories.append(category)
            
    return {
        "categories": unique_categories
    }

@app.get("/books/latest")
def get_latest_book():
    if len(books) == 0:
        return {
            "message": "No books available"
        }
        
    latest_book = books[0]
    
    for book in books:
        if book.get("year") > latest_book.get("year"):
            latest_book = book 
            
    return latest_book