from tkinter import Toplevel, Label, Entry, messagebox, StringVar, OptionMenu
import os
import uuid
import time

class SignInPage:
    def __init__(self, shared):
        self.shared = shared # Shared state object for cross-module data

    def sign_in_page(self):
        # Get shared resources
        mainpage = self.shared.mainpage
        cursor = self.shared.cursor
        conn = self.shared.conn

        # Create Sign In window
        sign_in_window = Toplevel(mainpage)
        sign_in_window.title("Sign In")
        sign_in_window.geometry("400x700")
        sign_in_window.resizable(False, False)
        sign_in_window.config(bg="white")

        header = Label(sign_in_window, text="Sign In", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        # --- USER INPUT FIELDS ---
        email_label = Label(sign_in_window, text="Email:", font=("Lora", 12), bg="white", fg="black")
        email_label.place(x=10, y=70, width=100, height=30)
        email_entry = Entry(sign_in_window, font=("Lora", 12), bg='white', fg="black")
        email_entry.place(x=120, y=70, width=250, height=30)

        password_label = Label(sign_in_window, text="Password:", font=("Lora", 12), bg="white", fg="black")
        password_label.place(x=10, y=110, width=100, height=30)
        password_entry = Entry(sign_in_window, font=("Lora", 12), show="*", bg='white', fg="black")
        password_entry.place(x=120, y=110, width=250, height=30)

        # --- LOGIN LOGIC ---
        def check_login():
            # Retrieve user input
            email = email_entry.get()
            password = password_entry.get()

            # Validate credentials from database
            cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            user = cursor.fetchone()
            if user:
                # Successful login
                self.shared.current_user_email = email
                # Generate session code and expiry (2 days)
                session_code = str(uuid.uuid4())
                expiry = int(time.time()) + 2 * 24 * 60 * 60

                # Save session information
                with open("session.txt", "w") as f:
                    f.write(f"{email}|{session_code}|{expiry}")
                self.shared.session_code = session_code
                messagebox.showinfo("Success", f"Welcome back, {user[1]}!")
                sign_in_window.destroy()
                self.shared.mainpage.deiconify()
                self.shared.update_mainpage_buttons() # Update main page buttons
            else:
                # Invalid credentials
                messagebox.showerror("Error", "Invalid email or password. Please try again.")

        # --- BUTTONS ---
        sign_in_button = Label(sign_in_window, text="Sign In", font=("Lora", 12), bg="#809D3C", fg="white")
        sign_in_button.place(x=20, y=160, width=360, height=30)
        sign_in_button.bind("<Button-1>", lambda event: check_login())

        sign_up_label = Label(sign_in_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="white")
        sign_up_label.place(x=20, y=200, width=175, height=30)
        sign_up_label.bind("<Button-1>", lambda e: (sign_in_window.destroy(), self.sign_up_page()))

        back_button = Label(sign_in_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
        back_button.place(x=205, y=200, width=175, height=30)
        back_button.bind("<Button-1>", lambda e: (sign_in_window.destroy(), mainpage.deiconify()))

    def sign_up_page(self):
        mainpage = self.shared.mainpage
        cursor = self.shared.cursor
        conn = self.shared.conn

        sign_up_window = Toplevel(mainpage)
        sign_up_window.title("Sign Up")
        sign_up_window.geometry("400x700")
        sign_up_window.resizable(False, False)
        sign_up_window.config(bg="white")

        header = Label(sign_up_window, text="Sign Up", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        # --- SIGN UP PAGE 1 FIELDS ---
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

        # --- PHONE NUMBER FIELD ---
        phone_label = Label(sign_up_window, text="Phone:*", font=("Lora", 12), bg="white", fg="black")
        phone_label.place(x=10, y=230, width=70, height=30)
        phone_entry = Entry(sign_up_window, font=("Lora", 12), bg='white', fg="black")
        phone_entry.place(x=120, y=230, width=250, height=30)

        password_label = Label(sign_up_window, text="Password:*", font=("Lora", 12), bg="white", fg="black")
        password_label.place(x=10, y=270, width=70, height=30)
        password_entry = Entry(sign_up_window, font=("Lora", 12), show="*", bg='white', fg="black")
        password_entry.place(x=120, y=270, width=250, height=30)

        gender_label = Label(sign_up_window, text="Gender:*", font=("Lora", 12), bg="white", fg="black")
        gender_label.place(x=10, y=310, width=70, height=30)
        gender_options = ["Male", "Female"]
        gender_var = StringVar(sign_up_window)
        gender_var.set(gender_options[0])
        gender_dropdown = OptionMenu(sign_up_window, gender_var, *gender_options)
        gender_dropdown.config(bg='white', fg="black")
        gender_dropdown.place(x=120, y=310, width=120, height=30)

        # --- SIGN UP PAGE 1 BUTTONS ---
        back_button = Label(sign_up_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
        back_button.place(x=10, y=310, width=180, height=30)
        def go_back(event):
            sign_up_window.destroy()
            self.sign_in_page()
        back_button.bind("<Button-1>", go_back)

        # --- SIGN UP PAGE 2 ---
        def second_signup_window():
            second_window = Toplevel(sign_up_window)
            second_window.title("Sign Up")
            second_window.geometry("400x700")
            second_window.config(bg="white")

            header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24), bg="#4F6F52", fg="white")
            header.place(x=10, y=10, width=380, height=50)

            # Clothing Size
            size_label = Label(second_window, text="Clothing Size:", font=("Lora", 12), bg="white", fg="black")
            size_label.place(x=10, y=70, width=180, height=30)
            size_options = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
            size_var = StringVar(second_window)
            size_var.set(size_options[0])
            size_dropdown = OptionMenu(second_window, size_var, *size_options)
            size_dropdown.config(bg='white', fg="black")
            size_dropdown.place(x=200, y=70, width=180, height=30)

            # Shoe Size
            shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12), bg="white", fg="black")
            shoe_size_label.place(x=10, y=110, width=180, height=30)
            shoe_size_options = [str(i) for i in range(1, 16)]
            shoe_size_var = StringVar(second_window)
            shoe_size_var.set(shoe_size_options[0])
            shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
            shoe_size_dropdown.config(bg='white', fg="black")
            shoe_size_dropdown.place(x=200, y=110, width=180, height=30)

            # --- SAVE USER TO DATABASE ---
            def save_user():
                cursor.execute(
                    'INSERT INTO users (first_name, last_name, email, password, gender, clothing_size, shoe_size, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    (
                        first_name_entry.get(),
                        last_name_entry.get(),
                        email_entry.get(),
                        password_entry.get(),
                        gender_var.get(),
                        size_var.get(),
                        shoe_size_var.get(),
                        phone_entry.get()
                    )
                )
                conn.commit()
                # session code and expiry (2 days)
                session_code = str(uuid.uuid4())
                expiry = int(time.time()) + 2 * 24 * 60 * 60
                with open("session.txt", "w") as f:
                    f.write(f"{email_entry.get()}|{session_code}|{expiry}")
                self.shared.current_user_email = email_entry.get()
                self.shared.session_code = session_code
                messagebox.showinfo("Success", "Sign up successful!")
                second_window.destroy()
                sign_up_window.destroy()
                mainpage.deiconify()

            sign_up_button = Label(second_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="White")
            sign_up_button.place(x=10, y=160, width=370, height=40)
            sign_up_button.bind("<Button-1>", lambda event: save_user())

        # Function to handle continue button click
        def handle_continue():
            # Check required fields
            if first_name_entry.get() == "" or last_name_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
                messagebox.showwarning("Missing Fields", "Please fill in all required fields.")
                return
            second_signup_window()

        continue_button = Label(sign_up_window, text="Continue", font=("Lora", 12), bg="#809D3C", fg="white")
        continue_button.place(x=200, y=310, width=180, height=30)
        continue_button.bind("<Button-1>", lambda e: handle_continue())

#Session check on app start (call this before showing main page)
def load_session(shared):
    import time
    if os.path.exists("session.txt"):
        with open("session.txt", "r") as f:
            data = f.read().strip().split("|")
            if len(data) == 3:
                email, session_code, expiry = data
                if int(expiry) > int(time.time()):
                    shared.current_user_email = email
                    shared.session_code = session_code
                else:
                    os.remove("session.txt")