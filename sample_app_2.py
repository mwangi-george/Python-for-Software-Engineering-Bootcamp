from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
import sqlite3


def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        bio TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Publishers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        publisher_id INTEGER,
        published_date TEXT,
        FOREIGN KEY (author_id) REFERENCES Authors (id),
        FOREIGN KEY (publisher_id) REFERENCES Publishers (id)
    )
    ''')

    conn.commit()
    conn.close()


# Initialize the database
init_db()


app = FastAPI()

DATABASE = 'books.db'

# Dependency to get a database connection


def get_db():
    conn = sqlite3.connect(DATABASE)
    try:
        yield conn
    finally:
        conn.close()

# Models


class Book(BaseModel):
    title: str
    author_id: int
    publisher_id: int
    published_date: str


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author_id: Optional[int] = None
    publisher_id: Optional[int] = None
    published_date: Optional[str] = None

# Endpoints


@app.post("/books", response_model=Book)
def create_book(book: Book, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO Books (title, author_id, publisher_id, published_date) VALUES (?, ?, ?, ?)",
        (book.title, book.author_id, book.publisher_id, book.published_date)
    )
    db.commit()
    book_id = cursor.lastrowid
    return {**book.dict(), "id": book_id}


@app.get("/books", response_model=List[Book])
def read_books(author_id: Optional[int] = None, publisher_id: Optional[int] = None, db: sqlite3.Connection = Depends(get_db)):
    query = "SELECT id, title, author_id, publisher_id, published_date FROM Books WHERE 1=1"
    params = []

    if author_id:
        query += " AND author_id = ?"
        params.append(author_id)
    if publisher_id:
        query += " AND publisher_id = ?"
        params.append(publisher_id)

    cursor = db.cursor()
    cursor.execute(query, params)
    books = cursor.fetchall()

    return [{"id": row[0], "title": row[1], "author_id": row[2], "publisher_id": row[3], "published_date": row[4]} for row in books]


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    update_data = book.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=400, detail="No fields provided for update")

    set_clause = ", ".join([f"{key} = ?" for key in update_data.keys()])
    values = list(update_data.values())
    values.append(book_id)

    cursor.execute(f"UPDATE Books SET {set_clause} WHERE id = ?", values)
    db.commit()

    cursor.execute(
        "SELECT id, title, author_id, publisher_id, published_date FROM Books WHERE id = ?", (book_id,))
    updated_book = cursor.fetchone()
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"id": updated_book[0], "title": updated_book[1], "author_id": updated_book[2], "publisher_id": updated_book[3], "published_date": updated_book[4]}


@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    db.commit()
    return {"detail": "Book deleted"}
