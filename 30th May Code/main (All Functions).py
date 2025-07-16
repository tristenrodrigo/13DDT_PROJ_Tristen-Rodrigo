from tkinter import Tk, Label, Button, Toplevel, Entry, StringVar, OptionMenu, messagebox, PhotoImage
import sqlite3
from PIL import Image, ImageTk


mainpage = Tk()

#Creating title and main window
mainpage.title("Loopwear") 
mainpage.geometry("400x700")
mainpage.config(bg="white")

#Creating Header
mainpage.grid_columnconfigure(0, weight=1)
header = Label(mainpage, text="Loopwear", font=("Lora", 24))
header.config(bg="#4F6F52", fg="white")
header.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

#Creating Header Bar
header_bar = Label(mainpage)
header_bar.config(bg='#809D3C')
header_bar.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

def open_sign_in_close_main(event):
    sign_in_page()
    mainpage.withdraw()

#Creating Sign Up Button (placed on top of the header bar)
sign_in_button = Label(mainpage, text="Sign In", font=("Lora", 12), bg="#5D8736", fg="black", anchor="w")
sign_in_button.grid(row=10, column=1, sticky="w", padx=10, pady=10) 
sign_in_button.bind("<Button-1>", open_sign_in_close_main)

#Search Bar
search_bar = Entry(mainpage, font=("Lora", 12), bg="white", fg="black")
search_bar.grid(row=1, column=0, sticky="w", padx=5, pady=5)

#Creating Search Button
search_button = Label(mainpage, text="Search", font=("Lora", 12), bg="#809D3C", fg="white")
search_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)
search_button.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Search functionality is under construction."))

#New listing button
new_listing_button = Label(mainpage, text="Create New Listing",font=("Lora", 12), bg="#809D3C", fg="white", anchor="center")
new_listing_button.grid(row=10, column=0, sticky="s", padx=10, pady=10)
new_listing_button.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "New listing functionality is under construction."))

#Creating Clothes Header
clothes_header = Label(mainpage, text="Clothes", font=("Lora", 18), bg="#5D8736", fg="white")
clothes_header.grid(row=2, column=0, sticky="w", padx=5, pady=5)
clothes_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Clothes section is under construction."))

#Creating Shoes Header
shoes_header = Label(mainpage, text="Shoes", font=("Lora", 18), bg="#5D8736", fg="white")
shoes_header.grid(row=4, column=0, sticky="w", padx=5, pady=5)
shoes_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Shoes section is under construction."))

#Creating Accessories Header
accessories_header = Label(mainpage, text="Accessories", font=("Lora", 18), bg="#5D8736", fg="white")
accessories_header.grid(row=6, column=0, sticky="w", padx=5, pady=5)
accessories_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Accessories section is under construction."))

#function to create the sign up page
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

    def open_mainpage_close_sign_in(event):
        mainpage.deiconify()
        sign_in_page.withdraw()

    # Back Button using Label
    back_button = Label(sign_in_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
    back_button.bind("<Button-1>", lambda event: (sign_in_window.destroy(), mainpage.deiconify()))

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

def listing_page():
    listing_window = Toplevel(mainpage)
    listing_window.title("Listing Page")
    listing_window.geometry("400x700")
    listing_window.config(bg="white")

    # Creating Header for the Listing page
    header = Label(listing_window, text="Listing ###", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #Main Image for Item
    main_image = Label(listing_window, text="Main Image", font=("Lora", 12), bg="white", fg="black")
    main_image.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    #Description Label
    description_label = Label(listing_window, text="Description:", font=("Lora", 12))
    description_label.config(bg="white", fg="black")
    description_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    #Description text
    description_text = Label(listing_window, text="This is a description of the item.", font=("Lora", 12))
    description_text.config(bg="white", fg="black")
    description_text.grid(row=2, column=1, sticky="w", padx=5, pady=5)

def new_listing_page():
    new_listing_window = Toplevel(mainpage)
    new_listing_window.title("New Listing")
    new_listing_window.geometry("400x700")
    new_listing_window.config(bg="white")

    # Creating Header for the New Listing page
    header = Label(new_listing_window, text="New Listing", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #Creating Item Name Label
    item_name_label = Label(new_listing_window, text="Item Name:", font=("Lora", 12))
    item_name_label.config(bg="white", fg="black")
    item_name_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    #Entry field for Item Name
    item_name_entry = Entry(new_listing_window, font=("Lora", 12))
    item_name_entry.config(bg='white', fg="black")
    item_name_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    
    #Item Image
    item_image_button = Button(new_listing_window, text="Choose Item Image", font=("Lora", 12))
    item_image_button.config(bg="white", fg="black")
    item_image_button.grid(row=1, column=2, sticky="w", padx=5, pady=5)
    item_image_button.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Image selection functionality is under construction."))
    
    #Creating Item Description Label
    item_description_label = Label(new_listing_window, text="Item Description:", font=("Lora", 12))
    item_description_label.config(bg="white", fg="black")
    item_description_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    #Entry field for Item Description
    item_description_entry = Entry(new_listing_window, font=("Lora", 12))
    item_description_entry.config(bg='white', fg="black")
    item_description_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Load and resize the image
original_image = Image.open("/Users/tristenrodrigo/Documents/School/13DDT/13DDT_PROJ_Tristen Rodrigo/Image/Shirt.png")
resized_image = original_image.resize((80, 80))
clothes_image = ImageTk.PhotoImage(resized_image)

#Clothes listing image button
clothes_listing_button = Button(mainpage, image=clothes_image, command=listing_page, bg="white")
clothes_listing_button.grid(row=3, column=0, sticky="w", padx=10, pady=10)

mainpage.mainloop()
