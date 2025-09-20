from V3.db import Database
from V3.shared import SharedState
from V3.mainpage import MainPage
from V3.signin import load_session

def main():
    # Initialize the database connection and setup tables if needed
    db = Database()
    # Create a shared state object for passing data between pages
    shared = SharedState()
    # Attach database objects to shared state for easy access
    shared.db = db
    shared.conn = db.conn
    shared.cursor = db.cursor
    # Load user session if it exists (auto-login)
    load_session(shared)
    # Start the main application window
    MainPage(shared)

if __name__ == "__main__":
    # Entry point for the application
    main()