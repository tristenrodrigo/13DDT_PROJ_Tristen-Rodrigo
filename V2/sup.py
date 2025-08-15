from tkinter import *
from tkinter import messagebox, StringVar, OptionMenu
from fisf2.base import mainpage, conn, cursor
from fisf2.sip import sign_in_page

def sign_up_page():
    sign_up_window = Toplevel(mainpage)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("400x700")
    sign_up_window.config(bg="white")

    header = Label(sign_up_window, text="Sign Up", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
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
    back_button.bind("<Button-1>", lambda e: (sign_up_window.destroy(), sign_in_page()))
        
    # Function to handle continue button click
    def handle_continue():
        gender = gender_var.get()
        # Check required fields
        if first_name_entry.get() == "" or last_name_entry.get() =="" or email_entry.get() == "" or password_entry.get() == "":
            messagebox.showwarning("Missing Fields", "Please fill in all required fields.")
            return  # Stop here, don't open the next page
        if gender == "Male":
            male_second_signup_window()
        elif gender == "Female":
            female_second_signup_window()
        elif gender == "Other":
            undefined_second_signup_window()

    # Continue Button to the next page
    continue_button = Label(sign_up_window, text="Continue", font=("Lora", 12), bg="#809D3C", fg="white")
    continue_button.place(x=200, y=310, width=180, height=30)
    continue_button.bind("<Button-1>", lambda e: handle_continue())

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