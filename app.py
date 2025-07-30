from cisf.db import Database
from cisf.shared import SharedState
from cisf.mainpage import MainPage

def main():
    shared = SharedState()
    shared.db = Database()
    shared.conn = shared.db.conn
    shared.cursor = shared.db.cursor
    MainPage(shared)

if __name__ == "__main__":
    main()