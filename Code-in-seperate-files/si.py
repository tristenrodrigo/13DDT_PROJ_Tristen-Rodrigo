from tkinter import Label, Toplevel, Entry, messagebox
from base import mainpage
from su import sign_up_page
import sqlite3

def sign_in_page():
    sign_in_window = Toplevel(mainpage)
    sign_in_window.title("Sign In")
    sign_in_window.geometry("400x700")
    sign_in_window.config(bg="white")

    header = Label(sign_in_window, text="Sign In", font=("Lora", 24), bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    email_label = Label(sign_in_window, text="Email:", font=("Lora", 12), bg="white", fg="black")
    email_label.place(x=10, y=70, width=100, height=30)
    email_entry = Entry(sign_in_window, font=("Lora", 12), bg='white', fg="black")
    email_entry.place(x=120, y=70, width=250, height=30)

    password_label = Label(sign_in_window, text="Password:", font=("Lora", 12), bg="white", fg="black")
    password_label.place(x=10, y=110, width=100, height=30)
    password_entry = Entry(sign_in_window, font=("Lora", 12), show="*", bg='white', fg="black")
    password_entry.place(x=120, y=110, width=250, height=30)

    def check_login():
        from base import update_mainpage_for_login
        global current_user_email
        email = email_entry.get()
        password = password_entry.get()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        if user:
            current_user_email = email  # Store the logged-in user's email
            messagebox.showinfo("Success", f"Welcome back, {user[1]}!")
            sign_in_window.destroy()
            mainpage.deiconify()
            update_mainpage_for_login()
        else:
            messagebox.showerror("Error", "Invalid email or password. Please try again.")

    sign_in_button = Label(sign_in_window, text="Sign In", font=("Lora", 12), bg="#809D3C", fg="white", anchor="center")
    sign_in_button.place(x=20, y=160, width=360, height=30)
    sign_in_button.bind("<Button-1>", lambda event: check_login())
    
    #Create Sign Up button
    sign_up_button = Label(sign_in_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="white")
    sign_up_button.place(x=20, y=200, width=175, height=30)
    sign_up_button.bind("<Button-1>", lambda event: (sign_in_window.withdraw(), sign_up_page()))

    # Back Button using Label
    back_button = Label(sign_in_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.place(x=205, y=200, width=175, height=30)
    back_button.bind("<Button-1>", lambda e: (sign_in_window.destroy(), mainpage.deiconify()))

# Create/connect to the database
conn = sqlite3.connect('listings.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
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
conn.commit()