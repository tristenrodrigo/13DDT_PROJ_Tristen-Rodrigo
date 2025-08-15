from V3.db import Database
from V3.shared import SharedState
from V3.mainpage import MainPage
from V3.signin import load_session

def main():
    shared = SharedState()
    shared.db = Database()
    shared.conn = shared.db.conn
    shared.cursor = shared.db.cursor
    load_session(shared)
    MainPage(shared)

if __name__ == "__main__":
    main()