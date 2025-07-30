from tkinter import Tk

class SharedState:
    def __init__(self):
        self.mainpage = None
        self.conn = None
        self.cursor = None
        self.current_user_email = None