import fisf1.db as db
import fisf1.mainpage as mainpage

if __name__ == "__main__":
    db.setup_db()
    mainpage.launch_mainpage()