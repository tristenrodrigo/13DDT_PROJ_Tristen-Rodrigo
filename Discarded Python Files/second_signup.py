from tkinter import *
from tkinter import messagebox, StringVar, OptionMenu
from fisf2.base import mainpage, cursor, conn
from si import *

def male_second_signup_window(first_name, last_name, email, password, gender):
    second_window = Toplevel(sign_up_window)
    second_window.title("Sign Up")
    second_window.geometry("400x700")
    second_window.config(bg="white")

    header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=10, y=10, width=380, height=50)

    # Clothing Size
    size_label = Label(second_window, text="Clothing Size:", font=("Lora", 12), bg="white", fg="black")
    size_label.place(x=10, y=70, width=180, height=30)
    size_options = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
    size_var = StringVar(second_window)
    if size_options:
        size_var.set(size_options[0])
    else:
        size_var.set("Default")
    size_dropdown = OptionMenu(second_window, size_var, *size_options)
    size_dropdown.config(bg='white', fg="black")
    size_dropdown.place(x=200, y=70, width=180, height=30)

    # Shoe Size
    shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12), bg="white", fg="black")
    shoe_size_label.place(x=10, y=110, width=180, height=30)
    shoe_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    shoe_size_var = StringVar(second_window)
    if shoe_size_options:
        shoe_size_var.set(shoe_size_options[0])
    else:
        shoe_size_var.set("Default")
    shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
    shoe_size_dropdown.config(bg='white', fg="black")
    shoe_size_dropdown.place(x=200, y=110, width=180, height=30)

    # Save user data to database
    def save_user():
        cursor.execute(
            'INSERT INTO users (first_name, last_name, email, password, gender, clothing_size, shoe_size) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (
                first_name,  # first name
                last_name,   # last name
                email,
                password,
                gender,
                size_var.get(),
                shoe_size_var.get()
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Sign up successful!")
        second_window.destroy()
        sign_up_window.destroy()
        mainpage.deiconify()

    sign_up_button = Label(second_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="White")
    sign_up_button.place(x=10, y=160, width=370, height=40)
    sign_up_button.bind("<Button-1>", lambda event: save_user())

def female_second_signup_window(first_name, last_name, email, password, gender):
    # Creating the second window
    second_window = Toplevel(sign_up_window)
    second_window.title("Sign Up")
    second_window.geometry("400x700")
    second_window.config(bg="white")

    # Creating Header for the second window
    header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=10, y=10, width=380, height=50)

    # Clothing Size Label
    size_label = Label(second_window, text="Clothing Size:", font=("Lora", 12))
    size_label.config(bg="white", fg="black")
    size_label.place(x=10, y=70, width=180, height=30)
    size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    size_var = StringVar(second_window)
    if size_options:
        size_var.set(size_options[0])
    else:
        size_var.set("Default")

    # Dropdown Menu
    size_dropdown = OptionMenu(second_window, size_var, *size_options)
    size_dropdown.config(bg='white', fg="black")
    size_dropdown.place(x=200, y=70, width=180, height=30)

    # Shoe Size Label
    shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12))
    shoe_size_label.config(bg="white", fg="black")
    shoe_size_label.place(x=10, y=110, width=180, height=30)
    shoe_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    shoe_size_var = StringVar(second_window)
    if shoe_size_options:
        shoe_size_var.set(shoe_size_options[0])
    else:
        shoe_size_var.set("Default")

    # Dropdown Menu
    shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
    shoe_size_dropdown.config(bg='white', fg="black")
    shoe_size_dropdown.place(x=200, y=110, width=180, height=30)

    # Save user data to database
    def save_user():
        cursor.execute(
            'INSERT INTO users (first_name, last_name, email, password, gender, clothing_size, shoe_size) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (
                first_name,  # first name
                last_name,  # last name
                email,
                password,
                gender,
                size_var.get(),
                shoe_size_var.get()
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Sign up successful!")
        second_window.destroy()
        sign_up_window.destroy()
        mainpage.deiconify()

    # Creating Sign Up Button
    sign_up_button = Label(second_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="White")
    sign_up_button.place(x=10, y=160, width=370, height=40)
    sign_up_button.bind("<Button-1>", lambda event: save_user())

def undefined_second_signup_window(first_name, last_name, email, password, gender):
    # Creating the second window
    second_window = Toplevel(sign_up_window)
    second_window.title("Sign Up")
    second_window.geometry("400x700")
    second_window.config(bg="white")

    # Creating Header for the second window
    header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=10, y=10, width=380, height=50)

    # Clothing Size Label Option 1
    size1_label = Label(second_window, text="Clothing Size:", font=("Lora", 12))
    size1_label.config(bg="white", fg="black")
    size1_label.place(x=10, y=70, width=180, height=30)
    size1_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    size1_var = StringVar(second_window)
    if size1_options:
        size1_var.set(size1_options[0])
    else:
        size1_var.set("Default")

    # Dropdown Menu for Clothing Size Option 1
    size1_dropdown = OptionMenu(second_window, size1_var, *size1_options)
    size1_dropdown.config(bg='white', fg="black")
    size1_dropdown.place(x=200, y=70, width=80, height=30)

    # Clothing Size option 2
    size2_options = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
    size2_var = StringVar(second_window)
    if size2_options:
        size2_var.set(size2_options[0])
    else:
        size2_var.set("Default")

    # Dropdown Menu for Clothing Size Option 2
    size2_dropdown = OptionMenu(second_window, size2_var, *size2_options)
    size2_dropdown.config(bg='white', fg="black")
    size2_dropdown.place(x=290, y=70, width=90, height=30)

    # Shoe Size Label
    shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12))
    shoe_size_label.config(bg="white", fg="black")
    shoe_size_label.place(x=10, y=110, width=180, height=30)
    shoe_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    shoe_size_var = StringVar(second_window)
    if shoe_size_options:
        shoe_size_var.set(shoe_size_options[0])
    else:
        shoe_size_var.set("Default")

    # Dropdown Menu
    shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
    shoe_size_dropdown.config(bg='white', fg="black")
    shoe_size_dropdown.place(x=200, y=110, width=180, height=30)

    # Save user data to database
    def save_user():
        cursor.execute(
            'INSERT INTO users (first_name, last_name, email, password, gender, clothing_size, shoe_size) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (
                first_name,  # first name
                last_name,   # last name
                email,
                password,
                gender,
                size1_var.get() if size1_var.get() else size2_var.get(),
                shoe_size_var.get()
            )
        )
        conn.commit()
        messagebox.showinfo("Success", "Sign up successful!")
        second_window.destroy()
        sign_up_window.destroy()
        mainpage.deiconify()

    sign_up_button = Label(second_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="White")
    sign_up_button.place(x=10, y=160, width=370, height=40)
    sign_up_button.bind("<Button-1>", lambda event: save_user())