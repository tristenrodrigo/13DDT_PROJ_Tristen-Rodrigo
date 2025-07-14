from tkinter import Toplevel, Label, Entry, messagebox
import fisf1.shared as shared

def sign_in_page():
    mainpage = shared.mainpage
    cursor = shared.cursor
    conn = shared.conn

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
        email = email_entry.get()
        password = password_entry.get()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        if user:
            shared.current_user_email = email
            messagebox.showinfo("Success", f"Welcome back, {user[1]}!")
            sign_in_window.destroy()
            shared.mainpage.deiconify()
            shared.update_mainpage_buttons()
        else:
            messagebox.showerror("Error", "Invalid email or password. Please try again.")

    sign_in_button = Label(sign_in_window, text="Sign In", font=("Lora", 12), bg="#809D3C", fg="white")
    sign_in_button.place(x=20, y=160, width=360, height=30)
    sign_in_button.bind("<Button-1>", lambda event: check_login())

    sign_up_label = Label(sign_in_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="white")
    sign_up_label.place(x=20, y=200, width=175, height=30)
    sign_up_label.bind("<Button-1>", lambda e: (sign_in_window.destroy(), mainpage.withdraw(), shared.launch_signup_page()))

    # Back Button
    back_button = Label(sign_in_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.place(x=205, y=200, width=175, height=30)
    back_button.bind("<Button-1>", lambda e: (sign_in_window.destroy(), mainpage.deiconify()))