import sqlite3

class Database:
    def __init__(self, db_path='lu.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        # Create listings table if it doesn't exist
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

        # Add contact_visibility column to listings if it doesn't exist
        try:
            self.cursor.execute("ALTER TABLE listings ADD COLUMN contact_visibility TEXT")
            self.conn.commit()
        except sqlite3.OperationalError:
            pass  # Column already exists

        # Create users table if it doesn't exist
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

        # Add phone column to users if it doesn't exist
        try:
            self.cursor.execute("ALTER TABLE users ADD COLUMN phone TEXT")
            self.conn.commit()
        except sqlite3.OperationalError:
            pass  # Column already exists

