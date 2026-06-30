from fastapi import FastAPI

app = FastAPI() #instance 

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Le Thi C",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Pham Van D",
        "category": "programming",
        "year": 2008,
        "is_available": False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vu Thi E",
        "category": "network",
        "year": 2019,
        "is_available": True
    }
]

@app.get("/books/available")
def get_available_books():
    available_books = []
    
    for book in books:
        if book.get("is_available") == True:
            available_books.append(book)
            
    return available_books

@app.get("/books/borrowed")
def get_borrowed_books():
    borrowed_books = []
    
    for book in books:
        if book.get("is_available") == False:
            borrowed_books.append(book)
            
    return borrowed_books