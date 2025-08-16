from V3.db import Database
from V3.shared import SharedState
from V3.mainpage import MainPage
from V3.signin import load_session

def main():
    db = Database()
    shared = SharedState()
    shared.db = db
    shared.conn = db.conn
    shared.cursor = db.cursor
    load_session(shared)
    MainPage(shared)

if __name__ == "__main__":
    main()