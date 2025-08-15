from tkinter import Toplevel, Label, Entry, StringVar, OptionMenu, messagebox
import fisf1.shared as shared

def sign_up_page():
    mainpage = shared.mainpage
    cursor = shared.cursor
    conn = shared.conn

    sign_up_window = Toplevel(mainpage)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("400x700")
    sign_up_window.config(bg="white")

    header = Label(sign_up_window, text="Sign Up", font=("Lora", 24), bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    first_name_label = Label(sign_up_window, text="First Name:*", font=("Lora", 12), bg="white", fg="black")
    first_name_label.place(x=10, y=110, width=70, height=30)
    first_name_entry = Entry(sign_up_window, font=("Lora", 12), bg='white', fg="black")
    first_name_entry.place(x=120, y=110, width=250, height=30)

    last_name_label = Label(sign_up_window, text="Last Name:*", font=("Lora", 12), bg="white", fg="black")
    last_name_label.place(x=10, y=150, width=70, height=30)
    last_name_entry = Entry(sign_up_window, font=("Lora", 12), bg='white', fg="black")
    last_name_entry.place(x=120, y=150, width=250, height=30)

    email_label = Label(sign_up_window, text="Email:*", font=("Lora", 12), bg="white", fg="black")
    email_label.place(x=10, y=190, width=70, height=30)
    email_entry = Entry(sign_up_window, font=("Lora", 12), bg='white', fg="black")
    email_entry.place(x=120, y=190, width=250, height=30)

    password_label = Label(sign_up_window, text="Password:*", font=("Lora", 12), bg="white", fg="black")
    password_label.place(x=10, y=230, width=70, height=30)
    password_entry = Entry(sign_up_window, font=("Lora", 12), show="*", bg='white', fg="black")
    password_entry.place(x=120, y=230, width=250, height=30)

    gender_label = Label(sign_up_window, text="Gender:*", font=("Lora", 12), bg="white", fg="black")
    gender_label.place(x=10, y=270, width=70, height=30)
    gender_options = ["Male", "Female", "Other"]
    gender_var = StringVar(sign_up_window)
    gender_var.set(gender_options[0])
    gender_dropdown = OptionMenu(sign_up_window, gender_var, *gender_options)
    gender_dropdown.config(bg='white', fg="black")
    gender_dropdown.place(x=120, y=270, width=120, height=30)

    back_button = Label(sign_up_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.place(x=10, y=310, width=180, height=30)
    def go_back(event):
        sign_up_window.destroy()
        from fisf1.signin import sign_in_page
        sign_in_page()
    back_button.bind("<Button-1>", go_back)

    def handle_continue():
        gender = gender_var.get()
        if first_name_entry.get() == "" or last_name_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
            messagebox.showwarning("Missing Fields", "Please fill in all required fields.")
            return
        # You can add more logic here for gender-specific second signup windows if needed
        # For now, just save the user
        cursor.execute(
            'INSERT INTO users (first_name, last_name, email, password, gender) VALUES (?, ?, ?, ?, ?)',
            (
                first_name_entry.get(),
                last_name_entry.get(),
                email_entry.get(),
                password_entry.get(),
                gender
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Sign up successful!")
        sign_up_window.destroy()
        mainpage.deiconify()

    continue_button = Label(sign_up_window, text="Continue", font=("Lora", 12), bg="#809D3C", fg="white")
    continue_button.place(x=200, y=310, width=180, height=30)
    continue_button.bind("<Button-1>", lambda e: handle_continue())