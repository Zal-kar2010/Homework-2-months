import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    conn.commit()

def insert_books():
    books = [
        ("1984", "George Orwell", 1949, "Dystopian", 328, 5),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 281, 3),
        ("Brave New World", "Aldous Huxley", 1932, "Science Fiction", 311, 4),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 2),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Novel", 214, 6),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 7),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Dystopian", 194, 3),
        ("Moby-Dick", "Herman Melville", 1851, "Adventure", 635, 2),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 1),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Philosophical", 671, 2)
    ]

    cursor.executemany("""
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)
    conn.commit()

def select_books():
    cursor.execute("SELECT * FROM books")
    all_books = cursor.fetchall()
    for book in all_books:
        print(book)

if __name__ == "__main__":
    create_table()
    insert_books()
    select_books()
    conn.close()