from tkinter import Tk

class SharedState:
    def __init__(self):
        # Reference to the main Tkinter window (main page)
        self.mainpage = None
        # Database connection object
        self.conn = None
        # Database cursor object
        self.cursor = None
        # Currently logged-in user's email
        self.current_user_email = None
        # Session code for the current session
        self.session_code = None