import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")  # включаем поддержку внешних ключей

def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    """)
    conn.commit()

def insert_genres():
    genres = [
        (1, "Dystopian"),
        (2, "Classic"),
        (3, "Fantasy"),
    ]
    cursor.executemany("INSERT OR IGNORE INTO genres (id, name) VALUES (?, ?)", genres)
    conn.commit()

def insert_books():
    books = [
        (1, "1984", "George Orwell", 1949, 328, 5, 1),
        (2, "To Kill a Mockingbird", "Harper Lee", 1960, 281, 3, 2),
        (3, "The Hobbit", "J.R.R. Tolkien", 1937, 310, 7, 3),
        (4, "Fahrenheit 451", "Ray Bradbury", 1953, 194, 3, 1),
        (5, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 180, 2, 2),
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO books 
        (id, name, author, publication_year, number_of_pages, number_of_copies, genre_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, books)
    conn.commit()

def select_books_with_genres():
    cursor.execute("""
        SELECT b.id, b.name, b.author, b.publication_year, g.name AS genre
        FROM books b
        JOIN genres g ON b.genre_id = g.id
        ORDER BY b.id
    """)
    for row in cursor.fetchall():
        print(row)

if __name__ == "__main__":
    create_tables()
    insert_genres()
    insert_books()
    select_books_with_genres()
    conn.close()