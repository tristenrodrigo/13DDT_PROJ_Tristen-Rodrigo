from tkinter import  Label, Button, Toplevel, StringVar, OptionMenu
from sign_up import sign_up_window


def male_second_signup_window():
    # Creating the second window
    second_window = Toplevel(sign_up_window)
    second_window.title("Sign Up")
    second_window.geometry("400x700")
    second_window.config(bg="white")

    # Creating Header for the second window
    header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #Clothing Size Label
    size_label = Label(second_window, text="Clothing Size:", font=("Lora", 12))
    size_label.config(bg="white", fg="black")
    size_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    size_options = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
    size_var = StringVar(second_window)
    size_var.set(size_options[0])

    #Dropdown Menu
    size_dropdown = OptionMenu(second_window, size_var, *size_options)
    size_dropdown.config(bg='white', fg="black")
    size_dropdown.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    #Shoe Size Label
    shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12))
    shoe_size_label.config(bg="white", fg="black")
    shoe_size_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    shoe_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    shoe_size_var = StringVar(second_window)
    shoe_size_var.set(shoe_size_options[0])

    #Dropdown Menu
    shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
    shoe_size_dropdown.config(bg='white', fg="black")
    shoe_size_dropdown.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    #Creating Sign Up Button
    sign_up_button = Button(second_window, text="Sign Up", font=("Lora", 12))
    sign_up_button.config(bg="#809D3C", fg="Black")
    sign_up_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

def female_second_signup_window():
    # Creating the second window
    second_window = Toplevel(sign_up_window)
    second_window.title("Sign Up")
    second_window.geometry("400x700")
    second_window.config(bg="white")

    # Creating Header for the second window
    header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #Clothing Size Label
    size_label = Label(second_window, text="Clothing Size:", font=("Lora", 12))
    size_label.config(bg="white", fg="black")
    size_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    size_var = StringVar(second_window)
    size_var.set(size_options[0])

    #Dropdown Menu
    size_dropdown = OptionMenu(second_window, size_var, *size_options)
    size_dropdown.config(bg='white', fg="black")
    size_dropdown.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    #Shoe Size Label
    shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12))
    shoe_size_label.config(bg="white", fg="black")
    shoe_size_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    shoe_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    shoe_size_var = StringVar(second_window)
    shoe_size_var.set(shoe_size_options[0])

    #Dropdown Menu
    shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
    shoe_size_dropdown.config(bg='white', fg="black")
    shoe_size_dropdown.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    #Creating Sign Up Button
    sign_up_button = Button(second_window, text="Sign Up", font=("Lora", 12))
    sign_up_button.config(bg="#809D3C", fg="Black")
    sign_up_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

def undefined_second_signup_window():
    # Creating the second window
    second_window = Toplevel(sign_up_window)
    second_window.title("Sign Up")
    second_window.geometry("400x700")
    second_window.config(bg="white")

    # Creating Header for the second window
    header = Label(second_window, text="Sign Up: Page 2", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #Clothing Size Label Option 1
    size1_label = Label(second_window, text="Clothing Size:", font=("Lora", 12))
    size1_label.config(bg="white", fg="black")
    size1_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    size1_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    size1_var = StringVar(second_window)
    size1_var.set(size1_options[0])

    #Dropdown Menu for Clothing Size Option 1
    size1_dropdown = OptionMenu(second_window, size1_var, *size1_options)
    size1_dropdown.config(bg='white', fg="black")
    size1_dropdown.grid(row=1, column=2, sticky="w", padx=5, pady=5)

    #Clothing Size option 2
    size2_options = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
    size2_var = StringVar(second_window)
    size2_var.set(size2_options[0])

    #Dropdown Menu for Clothing Size Option 2
    size2_dropdown = OptionMenu(second_window, size2_var, *size2_options)
    size2_dropdown.config(bg='white', fg="black")
    size2_dropdown.grid(row=1, column=2, sticky="w", padx=5, pady=5)

    #Shoe Size Label
    shoe_size_label = Label(second_window, text="Shoe Size:", font=("Lora", 12))
    shoe_size_label.config(bg="white", fg="black")
    shoe_size_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    shoe_size_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    shoe_size_var = StringVar(second_window)
    shoe_size_var.set(shoe_size_options[0])

    #Dropdown Menu
    shoe_size_dropdown = OptionMenu(second_window, shoe_size_var, *shoe_size_options)
    shoe_size_dropdown.config(bg='white', fg="black")
    shoe_size_dropdown.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    #Creating Sign Up Button
    sign_up_button = Button(second_window, text="Sign Up", font=("Lora", 12))
    sign_up_button.config(bg="#809D3C", fg="Black")
    sign_up_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)