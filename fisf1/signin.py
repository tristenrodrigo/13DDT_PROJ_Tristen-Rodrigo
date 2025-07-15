from tkinter import Toplevel, Label, Entry, messagebox, StringVar, OptionMenu
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
    sign_up_label.bind("<Button-1>", lambda e: (sign_in_window.destroy(), sign_up_page()))

    # Back Button
    back_button = Label(sign_in_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.place(x=205, y=200, width=175, height=30)
    back_button.bind("<Button-1>", lambda e: (sign_in_window.destroy(), mainpage.deiconify()))

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
        sign_in_page()
    back_button.bind("<Button-1>", go_back)

    def male_second_signup_window():
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
                    first_name_entry.get(),  # first name
                    last_name_entry.get(),  # last name
                    email_entry.get(),
                    password_entry.get(),
                    gender_var.get(),
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

    def female_second_signup_window():
        # Creating the second window
        second_window = Toplevel(sign_up_window)
        second_window.title("Sign Up")
        second_window.geometry("400x700")
        second_window.config(bg="white")

        # Creating Header for the second window
        header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24))
        header.config(bg="#4F6F52", fg="white")
        header.place(x=10, y=10, width=380, height=50)

        #Clothing Size Label
        size_label = Label(second_window, text="Clothing Size:", font=("Lora", 12))
        size_label.config(bg="white", fg="black")
        size_label.place(x=10, y=70, width=180, height=30)
        size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        size_var = StringVar(second_window)
        if size_options:
            size_var.set(size_options[0])
        else:
            size_var.set("Default")

        #Dropdown Menu
        size_dropdown = OptionMenu(second_window, size_var, *size_options)
        size_dropdown.config(bg='white', fg="black")
        size_dropdown.place(x=200, y=70, width=180, height=30)

        #Shoe Size Label
        shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12))
        shoe_size_label.config(bg="white", fg="black")
        shoe_size_label.place(x=10, y=110, width=180, height=30)
        shoe_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        shoe_size_var = StringVar(second_window)
        if shoe_size_options:
            shoe_size_var.set(shoe_size_options[0])
        else:
            shoe_size_var.set("Default")

        #Dropdown Menu
        shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
        shoe_size_dropdown.config(bg='white', fg="black")
        shoe_size_dropdown.place(x=200, y=110, width=180, height=30)

        # Save user data to database
        def save_user():
            cursor.execute(
                'INSERT INTO users (first_name, last_name, email, password, gender, clothing_size, shoe_size) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (
                    first_name_entry.get(),  # first name
                    last_name_entry.get(),  # last name
                    email_entry.get(),
                    password_entry.get(),
                    gender_var.get(),
                    size_var.get(),
                    shoe_size_var.get()
                )
            )
            conn.commit()
            messagebox.showinfo("Success", "Sign up successful!")
            second_window.destroy()
            sign_up_window.destroy()
            mainpage.deiconify()

        #Creating Sign Up Button
        sign_up_button= Label(second_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="White")
        sign_up_button.place(x=10, y=160, width=370, height=40)
        sign_up_button.bind("<Button-1>", lambda event: save_user())
        
        sign_up_button = Label(second_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="White")
        sign_up_button.place(x=10, y=160, width=370, height=40)
        sign_up_button.bind("<Button-1>", lambda event: save_user())

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

    # Continue Button to the next page
    continue_button = Label(sign_up_window, text="Continue", font=("Lora", 12), bg="#809D3C", fg="white")
    continue_button.place(x=200, y=315, width=180, height=30)
    continue_button.bind("<Button-1>", lambda e: handle_continue())