import sqlite3

class Database:
    def __init__(self, db_path='lu.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                image_path TEXT,
                category TEXT
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
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
        self.conn.commit()
