import sqlite3

def create_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    data = c.fetchone()
    conn.close()
    return data

def save_current_chapter(username, subject, chapter):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            username TEXT,
            subject TEXT,
            chapter TEXT
        )
    """)
    c.execute(
        "INSERT INTO progress VALUES (?, ?, ?)",
        (username, subject, chapter)
    )
    conn.commit()
    conn.close()

def save_current_chapter(username, subject, chapter):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            username TEXT,
            subject TEXT,
            chapter TEXT
        )
    """)

    c.execute(
        "INSERT INTO progress (username, subject, chapter) VALUES (?, ?, ?)",
        (username, subject, chapter)
    )

    conn.commit()
    conn.close()
