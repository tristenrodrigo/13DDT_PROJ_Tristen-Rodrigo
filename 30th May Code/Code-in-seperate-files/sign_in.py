from tkinter import Label, Toplevel, Entry
from main import mainpage
from sign_up import sign_up_page

def sign_in_page():
    sign_in_window = Toplevel(mainpage)
    sign_in_window.title("Sign In")
    sign_in_window.geometry("400x700")
    sign_in_window.config(bg="white")

    # Grid for the sign in window
    sign_in_window.grid_columnconfigure(0, weight=1)

    #Creating Header for the Sign In page
    header = Label(sign_in_window, text="Sign In", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #Email Label
    email_label = Label(sign_in_window, text="Email:", font=("Lora", 12))
    email_label.config(bg="white", fg="black")
    email_label.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    #Entry field for email
    email_entry = Entry(sign_in_window, font=("Lora", 12))
    email_entry.config(bg='white', fg="black")
    email_entry.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    #Password Label
    password_label = Label(sign_in_window, text="Password:", font=("Lora", 12))
    password_label.config(bg="white", fg="black")
    password_label.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    #Entry field for password
    password_entry = Entry(sign_in_window, font=("Lora", 12), show="*")
    password_entry.config(bg='white', fg="black")
    password_entry.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

    #Creating Sign In Button
    sign_in_button = Label(sign_in_window, text="Sign In", font=("Lora", 12), bg="#809D3C", fg="white")
    sign_in_button.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    #Create Sign Up button
    sign_up_button = Label(sign_in_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="white")
    sign_up_button.grid(row=6, column=0, sticky="we", padx=5, pady=5)
    sign_up_button.bind("<Button-1>", lambda event: (sign_in_window.withdraw(), sign_up_page()))