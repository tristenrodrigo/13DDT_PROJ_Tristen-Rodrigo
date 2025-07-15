import cisf.db as db
import cisf.mainpage as mainpage

def main():
    db.setup_db()
    mainpage.launch_mainpage()

if __name__ == "__main__":
    main()