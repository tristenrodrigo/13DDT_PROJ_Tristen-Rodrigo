from tkinter import Label, Button, Toplevel, Entry, StringVar, OptionMenu, messagebox
from main import mainpage
from sign_in import sign_in_page
from second_signup import female_second_signup_window, male_second_signup_window, undefined_second_signup_window


def sign_up_page():
    sign_up_window = Toplevel(mainpage)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("400x700")
    sign_up_window.config(bg="white")
    
    # Grid for the sign up window
    sign_up_window.grid_columnconfigure(0, weight=1)

    # Creating Header for the Sign Up page
    header = Label(sign_up_window, text="Sign Up", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #Profile Picture
    profile_picture_button = Button(sign_up_window, text="Chose a Profile Picture", font=("Lora", 12))
    profile_picture_button.config(bg="white", fg="black")
    profile_picture_button.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    # creating sign up section
    first_name_label = Label(sign_up_window, text="First Name:*", font=("Lora", 12))
    first_name_label.config(bg="white", fg="black")
    first_name_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    # Entry field for name
    name_entry = Entry(sign_up_window, font=("Lora", 12))
    name_entry.config(bg='white', fg="black")
    name_entry.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    
    # Creating Last Name Label
    last_name_label = Label(sign_up_window, text="Last Name:*", font=("Lora", 12))
    last_name_label.config(bg="white", fg="black")
    last_name_label.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    # Entry field for name
    name_entry = Entry(sign_up_window, font=("Lora", 12))
    name_entry.config(bg='white', fg="black")
    name_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

    # Creating Email Label
    email_label = Label(sign_up_window, text="Email:*", font=("Lora", 12))
    email_label.config(bg="white", fg="black")
    email_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

    # Entry field for email
    email_entry = Entry(sign_up_window, font=("Lora", 12))
    email_entry.config(bg='white', fg="black")
    email_entry.grid(row=5, column=0, sticky="w", padx=5, pady=5)

    #Creating Password Label
    password_label = Label(sign_up_window, text="Password:*", font=("Lora", 12))
    password_label.config(bg="white", fg="black")
    password_label.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    #Entry Field for Password
    password_entry = Entry(sign_up_window, font=("Lora", 12), show="*")
    password_entry.config(bg='white', fg="black")
    password_entry.grid(row=5, column=1, sticky="w", padx=5, pady=5)

    #Entry for Gender
    gender_label = Label(sign_up_window, text="Gender:*", font=("Lora", 12))
    gender_label.config(bg="white", fg="black")
    gender_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
    gender_options = ["Male", "Female", "Other"]
    gender_var = StringVar(sign_up_window)
    gender_var.set(gender_options[0])

    #Dropdown Menu for Gender
    gender_dropdown = OptionMenu(sign_up_window, gender_var, *gender_options)
    gender_dropdown.config(bg='white', fg="black")
    gender_dropdown.grid(row=6, column=1, sticky="w", padx=5, pady=5)

    def open_sign_in_close_signup(event):
        sign_in_page()
        sign_up_window.withdraw()

    # Back Button using Label
    back_button = Label(sign_up_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
    back_button.bind("<Button-1>", lambda e: (sign_up_window.destroy(), sign_in_page()))

     # Function to handle continue button click
    def handle_continue():
        gender = gender_var.get()
        # Check required fields
        if name_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
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
    continue_button.grid(row=7, column=1, sticky="ew", padx=5, pady=5)
    continue_button.bind("<Button-1>", lambda e: handle_continue())