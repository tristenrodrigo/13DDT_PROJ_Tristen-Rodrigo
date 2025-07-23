import sqlite3
import cisf.shared as shared

def setup_db():
    shared.conn = sqlite3.connect('lu.db')
    shared.cursor = shared.conn.cursor()
    cursor = shared.cursor
    conn = shared.conn

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            image_path TEXT,
            category TEXT
        )
    ''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            password TEXT,
            gender TEXT,
            clothing_size TEXT,
            shoe_size TEXT
        )
    ''')
    conn.commit()