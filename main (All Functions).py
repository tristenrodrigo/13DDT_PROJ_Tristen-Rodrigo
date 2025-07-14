from tkinter import Label, Entry, messagebox, Toplevel, StringVar, OptionMenu,Tk, filedialog
from PIL import Image, ImageTk
import sqlite3
import time
import os

# Initialize current_user_email
current_user_email = None

# Create/connect to the database
conn = sqlite3.connect('.db')
cursor = conn.cursor()

# Create the listings table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name 
        TEXT NOT NULL,
        description TEXT)
''')
conn.commit()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        gender TEXT,
        clothing_size TEXT,
        shoe_size TEXT
    )
''')
conn.commit()

# Add image_path column if it doesn't exist
try:
    cursor.execute("ALTER TABLE listings ADD COLUMN image_path TEXT")
    conn.commit()
except sqlite3.OperationalError:
    pass  # Column already exists, ignore error

# Add category column if it doesn't exist
try:
    cursor.execute("ALTER TABLE listings ADD COLUMN category TEXT")
    conn.commit()
except sqlite3.OperationalError:
    pass  # Column already exists


mainpage = Tk()

#Creating title and main window
mainpage.title("Loopwear") 
mainpage.geometry("400x700")
mainpage.config(bg="white")

#Creating Header
mainpage.grid_columnconfigure(0, weight=1)
header = Label(mainpage, text="Loopwear", font=("Lora", 24))
header.config(bg="#4F6F52", fg="white")
header.place(x=0, y=0, width=400, height=60)

#Creating Header Bar
header_bar = Label(mainpage)
header_bar.config(bg='#809D3C')
header_bar.place(x=0, y=60, width=400, height=40)

def sign_in_page():
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
        global current_user_email
        email = email_entry.get()
        password = password_entry.get()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        if user:
            current_user_email = email
            with open("session.txt", "w") as f:
                f.write(email)
            messagebox.showinfo("Success", f"Welcome back, {user[1]}!")
            sign_in_window.destroy()
            mainpage.deiconify()
            update_mainpage_for_login()
        else:
            messagebox.showerror("Error", "Invalid Email or Password. Please try again.")

    sign_in_button = Label(sign_in_window, text="Sign In", font=("Lora", 12), bg="#809D3C", fg="white", anchor="center")
    sign_in_button.place(x=20, y=160, width=360, height=30)
    sign_in_button.bind("<Button-1>", lambda event: check_login())
    
    #Create Sign Up button
    sign_up_button = Label(sign_in_window, text="Sign Up", font=("Lora", 12), bg="#809D3C", fg="white")
    sign_up_button.place(x=20, y=200, width=175, height=30)
    sign_up_button.bind("<Button-1>", lambda event: (sign_in_window.withdraw(), sign_up_page()))

    # Back Button using Label
    back_button = Label(sign_in_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.place(x=205, y=200, width=175, height=30)
    back_button.bind("<Button-1>", lambda e: (sign_in_window.destroy(), mainpage.deiconify()))

def sign_up_page():
    sign_up_window = Toplevel(mainpage)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("400x700")
    sign_up_window.config(bg="white")

    header = Label(sign_up_window, text="Sign Up", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    first_name_label = Label(sign_up_window, text="First Name:*", font=("Lora", 12), bg="white", fg="black")
    first_name_label.place(x=10, y=75, width=70, height=30)
    first_name_entry = Entry(sign_up_window, font=("Lora", 12), bg='white', fg="black")
    first_name_entry.place(x=120, y=75, width=250, height=30)

    last_name_label = Label(sign_up_window, text="Last Name:*", font=("Lora", 12), bg="white", fg="black")
    last_name_label.place(x=10, y=115, width=70, height=30)
    last_name_entry = Entry(sign_up_window, font=("Lora", 12), bg='white', fg="black")
    last_name_entry.place(x=120, y=115, width=250, height=30)

    email_label = Label(sign_up_window, text="Email:*", font=("Lora", 12), bg="white", fg="black")
    email_label.place(x=10, y=155, width=70, height=30)
    email_entry = Entry(sign_up_window, font=("Lora", 12), bg='white', fg="black")
    email_entry.place(x=120, y=155, width=250, height=30)

    password_label = Label(sign_up_window, text="Password:*", font=("Lora", 12), bg="white", fg="black")
    password_label.place(x=10, y=195, width=70, height=30)
    password_entry = Entry(sign_up_window, font=("Lora", 12), show="*", bg='white', fg="black")
    password_entry.place(x=120, y=195, width=250, height=30)

    gender_label = Label(sign_up_window, text="Gender:*", font=("Lora", 12), bg="white", fg="black")
    gender_label.place(x=10, y=235, width=70, height=30)
    gender_options = ["Male", "Female", "Other"]
    gender_var = StringVar(sign_up_window)
    gender_var.set(gender_options[0])
    gender_dropdown = OptionMenu(sign_up_window, gender_var, *gender_options)
    gender_dropdown.config(bg='white', fg="black")
    gender_dropdown.place(x=120, y=235, width=120, height=30)

    back_button = Label(sign_up_window, text="Back", bg="#809D3C", fg="white", font=("Lora", 12))
    back_button.place(x=10, y=315, width=180, height=30)
    back_button.bind("<Button-1>", lambda e: (sign_up_window.destroy(), sign_in_page()))

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

def open_sign_in_close_main(event):
    sign_in_page()
    mainpage.withdraw()

#Creating Sign Up Button (placed on top of the header bar)
sign_in_button = Label(mainpage, text="Sign In", font=("Lora", 12), bg="#5D8736", fg="white", anchor="center")
sign_in_button.place(x=270, y=650, width=120, height=40)
sign_in_button.bind("<Button-1>", open_sign_in_close_main)

#Search Bar
search_bar = Entry(mainpage, font=("Lora", 12), bg="white", fg="black")
search_bar.place(x=10, y=70, width=250, height=20)

#search functionality
def display_category_listings():
    category = "Clothes"  # Example category, you can change this to filter by other categories
    cursor.execute("SELECT * FROM listings WHERE category=?", (category,))
    listings = cursor.fetchall()
    if not listings:
        messagebox.showinfo("Info", "No listings found in this category.")
        return

    listings_window = Toplevel(mainpage)
    listings_window.title(f"{category} Listings")
    listings_window.geometry("400x700")
    listings_window.config(bg="white")

    header = Label(listings_window, text=f"{category} Listings", font=("Lora", 24), bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    for index, listing in enumerate(listings):
        listing_label = Label(listings_window, text=f"{listing[1]} - {listing[2]}", font=("Lora", 12), bg="white", fg="black")
        listing_label.place(x=10, y=70 + index * 30, width=380, height=30)


#Creating Search Button
search_button = Label(mainpage, text="Search", font=("Lora", 12), bg="#809D3C", fg="white")
search_button.place(x=270, y=70, width=120, height=20)
search_button.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Search functionality is under construction."))

def new_listing_page():
    new_listing_window = Toplevel(mainpage)
    new_listing_window.title("New Listing")
    new_listing_window.geometry("400x700")
    new_listing_window.config(bg="white")

    header = Label(new_listing_window, text="New Listing", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    uploaded_image_label = Label(new_listing_window, bg="white")
    uploaded_image_label.place(x=10, y=70, width=180, height=180)

    # Store the image path in a mutable object
    image_path = {"path": None}

    def upload_image():
        file_path = filedialog.askopenfilename(
            title='Select an Image',
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*")]
        )
        if file_path:
            try:
                img = Image.open(file_path)
                img = img.resize((100, 100))
                photo = ImageTk.PhotoImage(img)
                uploaded_image_label.config(image=photo)
                uploaded_image_label.image = photo
                image_path["path"] = file_path  # Save the path for later
            except Exception:
                messagebox.showerror("Error", "Could not open image file.")

    image_upload_button = Label(new_listing_window, text="Upload Image", font=("Lora", 12), bg="#809D3C", fg="black")
    image_upload_button.place(x=110, y=70, width=180, height=30)
    image_upload_button.bind("<Button-1>", lambda event: upload_image())

    item_name_label = Label(new_listing_window, text="Item Name:", font=("Lora", 12), bg="white", fg="black")
    item_name_label.place(x=10, y=260, width=70, height=30)
    item_name_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")
    item_name_entry.place(x=200, y=260, width=180, height=30)

    item_description_label = Label(new_listing_window, text="Item Description:", font=("Lora", 12), bg="white", fg="black")
    item_description_label.place(x=10, y=300, width=100, height=30)
    item_description_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")
    item_description_entry.place(x=200, y=300, width=180, height=30)

    #Dropdown Menu for Item Category
    category_label = Label(new_listing_window, text="Item Category:*", font=("Lora", 12), bg="white", fg="black")
    category_label.place(x=10, y=340, width=100, height=30)
    category_options = ["Clothes", "Shoes", "Accessories"]
    category_var = StringVar(new_listing_window)
    category_var.set(category_options[0])
    category_dropdown = OptionMenu(new_listing_window, category_var, *category_options)
    category_dropdown.config(bg='white', fg="black")
    category_dropdown.place(x=120, y=340, width=120, height=30)
    
    def save_listing():
        name = item_name_entry.get()
        description = item_description_entry.get()
        img_path = image_path["path"]
        category = category_var.get()
        if not name:
            messagebox.showwarning("Missing Name", "Please enter an item name.")
            return
        cursor.execute(
            'INSERT INTO listings (name, description, image_path, category) VALUES (?, ?, ?, ?)',
            (name, description, img_path, category)
        )
        conn.commit()
        messagebox.showinfo("Info", "Listing saved successfully!")
        new_listing_window.destroy()
        mainpage.deiconify()
        display_category_listings()

    publish_listing_button = Label(new_listing_window, text="Publish Listing", font=("Lora", 12), bg="#809D3C", fg="white")
    publish_listing_button.place(x=10, y=400, width=370, height=40)
    publish_listing_button.bind("<Button-1>", lambda event: save_listing())

# New Listing Button
def open_new_listing_if_signed_in(event):
    global current_user_email
    if current_user_email:
        new_listing_page()
    else:
        messagebox.showwarning("Sign In Required", "Please sign in again to create a new listing.")
        # Optionally, force sign out here
        current_user_email = None

new_listing_button = Label(mainpage, text="Create New Listing", font=("Lora", 12), bg="#809D3C", fg="white", anchor="center")
new_listing_button.place(x=10, y=650, width=180, height=40)
new_listing_button.bind("<Button-1>", open_new_listing_if_signed_in)

def clothes_page():
    clothes_window = Toplevel(mainpage)
    clothes_window.title("Clothes")
    clothes_window.geometry("400x700")
    clothes_window.config(bg="white")

    header = Label(clothes_window, text="Clothes", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    # Back Button
    back_button = Label(clothes_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
    back_button.place(x=10, y=650, width=370, height=40)
    back_button.bind("<Button-1>", lambda event: (clothes_window.destroy(), mainpage.deiconify()))

#Creating Clothes Header
clothes_header = Label(mainpage, text="Clothes", font=("Lora", 18), bg="#5D8736", fg="white")
clothes_header.place(x=10, y=120, width=180, height=40)
clothes_header.bind("<Button-1>", lambda event: (clothes_page(), mainpage.withdraw()))

def display_category_listings():
    # Remove old listing labels if any
    for widget in mainpage.winfo_children():
        if getattr(widget, "is_listing_label", False):
            widget.destroy()

    # Clothes
    cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Clothes'")
    clothes_listings = cursor.fetchall()
    y_offset = 180
    for listing in clothes_listings:
        img_label = Label(mainpage, text=listing[1], font=("Lora", 12), bg="black", fg="white")
        img_label.place(x=10, y=y_offset, width=100, height=100)
        img_label.is_listing_label = True  # Mark for easy removal
        img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), mainpage.withdraw()))
        y_offset += 120

    # Shoes
    cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Shoes'")
    shoes_listings = cursor.fetchall()
    y_offset = 360
    for listing in shoes_listings:
        img_label = Label(mainpage, text=listing[1], font=("Lora", 12), bg="black", fg="white")
        img_label.place(x=10, y=y_offset, width=100, height=100)
        img_label.is_listing_label = True
        img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), mainpage.withdraw()))
        y_offset += 120

    # Accessories
    cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Accessories'")
    accessories_listings = cursor.fetchall()
    y_offset = 540
    for listing in accessories_listings:
        img_label = Label(mainpage, text=listing[1], font=("Lora", 12), bg="black", fg="white")
        img_label.place(x=10, y=y_offset, width=100, height=100)
        img_label.is_listing_label = True
        img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), mainpage.withdraw()))
        y_offset += 120

#listing Image Test
clothes_listing_image1 = Label(mainpage, text="Listing Image", font=("Lora", 12), bg="black", fg="black")
clothes_listing_image1.place(x=10, y=180, width=100, height=100)
clothes_listing_image1.bind("<Button-1>", lambda event: (listing_page(), mainpage.withdraw()))

def shoes_page():
    shoes_window = Toplevel(mainpage)
    shoes_window.title("Shoes")
    shoes_window.geometry("400x700")
    shoes_window.config(bg="white")

    header = Label(shoes_window, text="Shoes", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    # Back Button
    back_button = Label(shoes_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
    back_button.place(x=10, y=650, width=370, height=40)
    back_button.bind("<Button-1>", lambda event: (shoes_window.destroy(), mainpage.deiconify()))

#Creating Shoes Header
shoes_header = Label(mainpage, text="Shoes", font=("Lora", 18), bg="#5D8736", fg="white")
shoes_header.place(x=10, y=300, width=180, height=40)
shoes_header.bind("<Button-1>", lambda event: (shoes_page(), mainpage.withdraw()))

#listing Image Test
Shoes_listing_image2 = Label(mainpage, text="Listing Image", font=("Lora", 12), bg="black", fg="black")
Shoes_listing_image2.place(x=10, y=360, width=100, height=100)
Shoes_listing_image2.bind("<Button-1>", lambda event: (listing_page(), mainpage.withdraw()))

def accessories_page():
    accessories_window = Toplevel(mainpage)
    accessories_window.title("Accessories")
    accessories_window.geometry("400x700")
    accessories_window.config(bg="white")

    header = Label(accessories_window, text="Accessories", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    # Back Button
    back_button = Label(accessories_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
    back_button.place(x=10, y=650, width=370, height=40)
    back_button.bind("<Button-1>", lambda event: (accessories_window.destroy(), mainpage.deiconify()))

#Creating Accessories Header
accessories_header = Label(mainpage, text="Accessories", font=("Lora", 18), bg="#5D8736", fg="white")
accessories_header.place(x=10, y=480, width=180, height=40)
accessories_header.bind("<Button-1>", lambda event: (accessories_page(), mainpage.withdraw()))

#listing Image Test
accessories_listing_image3 = Label(mainpage, text="Listing Image", font=("Lora", 12), bg="black", fg="black")
accessories_listing_image3.place(x=10, y=540, width=100, height=100)
accessories_listing_image3.bind("<Button-1>", lambda event: (listing_page(), mainpage.withdraw()))

def listing_page(listing_id=None):
    listing_window = Toplevel(mainpage)
    listing_window.title("Listing Page")
    listing_window.geometry("400x700")
    listing_window.config(bg="white")

    if listing_id:
        cursor.execute("SELECT name, description, image_path FROM listings WHERE id=?", (listing_id,))
    else:
        cursor.execute("SELECT name, description, image_path FROM listings ORDER BY id DESC LIMIT 1")
    listing = cursor.fetchone()

    header = Label(listing_window, text=listing[0] if listing else "Listing", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=10, y=10, width=380, height=50)

    # Display the image if available
    main_image = Label(listing_window, bg="white")
    main_image.place(x=10, y=70, width=180, height=180)
    if listing and listing[2]:
        try:
            img = Image.open(listing[2])
            img = img.resize((100, 100))
            photo = ImageTk.PhotoImage(img)
            main_image.config(image=photo)
            main_image.image = photo
        except Exception:
            main_image.config(text="Image not found", fg="red")

    description_label = Label(listing_window, text="Description:", font=("Lora", 12))
    description_label.config(bg="white", fg="black")
    description_label.place(x=10, y=260, width=180, height=30)

    description_text = Label(listing_window, text=listing[1] if listing else "", font=("Lora", 12))
    description_text.config(bg="white", fg="black")
    description_text.place(x=200, y=260, width=180, height=30)

    back_button = Label(listing_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
    back_button.place(x=10, y=650, width=370, height=40)
    back_button.bind("<Button-1>", lambda event: (listing_window.destroy(), mainpage.deiconify()))
    
def update_mainpage_for_login():
    sign_in_button.place_forget()
    manage_account_button.place(x=270, y=650, width=120, height=40)

#Manage Account Page
def manage_account_page():
    manage_account_window = Toplevel(mainpage)
    manage_account_window.title("Manage Account")
    manage_account_window.geometry("400x700")
    manage_account_window.config(bg="white")

    header = Label(manage_account_window, text="Manage Account", font=("Lora", 24), bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)
     
    # Fetch user data from the database
    global current_user_email
    user_info = None
    if current_user_email:
        cursor.execute("SELECT first_name, last_name, email, gender, clothing_size, shoe_size FROM users WHERE email=?", (current_user_email,))
        user_info = cursor.fetchone()

    # User Information
    user_info_label = Label(manage_account_window, text="Account Info", font=("Lora", 18), bg="#A9C46C", fg="white")
    user_info_label.place(x=10, y=100, width=180, height=30)
    if user_info:
        info_text = f"Name: {user_info[0]} {user_info[1]}\nEmail: {user_info[2]}\nGender: {user_info[3]}\nClothing Size: {user_info[4]}\nShoe Size: {user_info[5]}"
    else:
        info_text = "No user info found."

    user_info_text = Label(manage_account_window, text=info_text, font=("Lora", 12), bg="white", fg="black", justify="left", anchor="nw")
    user_info_text.place(x=10, y=200, width=380, height=100)

    #Edit User Information Button
    edit_info_button = Label(manage_account_window, text="Edit Information", font=("Lora", 12), bg="#809D3C", fg="white")
    edit_info_button.place(x=10, y=410, width=370, height=40)
    def on_edit_info(event):
        edit_user_info()
        manage_account_window.withdraw()

    edit_info_button.bind("<Button-1>", on_edit_info)

    def edit_user_info():
        edit_window = Toplevel(manage_account_window)
        edit_window.title("Edit User Information")
        edit_window.geometry("400x700")
        edit_window.config(bg="white")
        header = Label(edit_window, text="Edit User Information", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        if user_info:
            first_name_label = Label(edit_window, text="First Name:", font=("Lora", 12), bg="white", fg="black")
            first_name_label.place(x=10, y=70, width=100, height=30)
            first_name_entry = Entry(edit_window, font=("Lora", 12), bg='white', fg="black")
            first_name_entry.place(x=120, y=70, width=250, height=30)
            first_name_entry.insert(0, user_info[0])

            last_name_label = Label(edit_window, text="Last Name:", font=("Lora", 12), bg="white", fg="black")
            last_name_label.place(x=10, y=110, width=100, height=30)
            last_name_entry = Entry(edit_window, font=("Lora", 12), bg='white', fg="black")
            last_name_entry.place(x=120, y=110, width=250, height=30)
            last_name_entry.insert(0, user_info[1])

            email_label = Label(edit_window, text="Email:", font=("Lora", 12), bg="white", fg="black")
            email_label.place(x=10, y=150, width=100, height=30)
            email_entry = Entry(edit_window, font=("Lora", 12), bg='white', fg="black")
            email_entry.place(x=120, y=150, width=250, height=30)
            email_entry.insert(0, user_info[2])

            password_label = Label(edit_window, text="Password:", font=("Lora", 12), bg="white", fg="black")
            password_label.place(x=10, y=190, width=100, height=30)
            password_entry = Entry(edit_window, font=("Lora", 12), show="*", bg='white', fg="black")
            password_entry.place(x=120, y=190, width=250, height=30)

        def save_info():
            new_first_name = first_name_entry.get()
            new_last_name = last_name_entry.get()
            new_email = email_entry.get()
            new_password = password_entry.get()

            if not new_first_name or not new_last_name or not new_email or not new_password:
                messagebox.showwarning("Input Error", "All fields are required.")
                return

            cursor.execute("UPDATE users SET first_name=?, last_name=?, email=?, password=? WHERE email=?", 
                           (new_first_name, new_last_name, new_email, new_password, current_user_email))
            conn.commit()
            messagebox.showinfo("Success", "User information updated successfully!")
            edit_window.destroy()
            manage_account_page()

        #Save Info Button
        save_info_button = Label(edit_window, text="Save Info", font=("Lora", 12), bg="#809D3C", fg="white")
        save_info_button.place(x=10, y=230, width=370, height=40)
        save_info_button.bind("<Button-1>", lambda event: save_info(), manage_account_window.deiconify())

    # Back to Main Page Button
    back_button = Label(manage_account_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
    back_button.place(x=10, y=650, width=370, height=40)
    back_button.bind("<Button-1>", lambda event: (manage_account_window.destroy(), mainpage.deiconify()))

    #Sign Out Button
    sign_out_button = Label(manage_account_window, text="Sign Out", font=("Lora", 12), bg="#809D3C", fg="white")
    sign_out_button.place(x=10, y=600, width=370, height=40)

    def update_mainpage_for_logout():
        global current_user_email
        current_user_email = None
        sign_in_button.place(x=270, y=650, width=120, height=40)
        manage_account_button.place_forget()

    def handle_sign_out(event):
        global current_user_email
        manage_account_window.destroy()
        mainpage.deiconify()
        current_user_email = None
        # Remove session file
        import os
        if os.path.exists("session.txt"):
            os.remove("session.txt")
        update_mainpage_for_logout()
    sign_out_button.bind("<Button-1>", handle_sign_out)

manage_account_button = Label(mainpage, text="Manage Account", font=("Lora", 12), bg="#5D8736", fg="white", anchor="w")
def manage_account(event):
    global current_user_email
    if current_user_email:
        manage_account_page()
        mainpage.withdraw()
    else:
        messagebox.showwarning("Session Expired", "Please sign in again to manage your account.")
        current_user_email = None
manage_account_button.bind("<Button-1>", manage_account)

# Check for existing session
if os.path.exists("session.txt"):
    with open("session.txt", "r") as f:
        saved_email = f.read().strip()
        cursor.execute("SELECT * FROM users WHERE email=?", (saved_email,))
        user = cursor.fetchone()
        if user:
            current_user_email = saved_email
            # Hide sign in, show manage account
            try:
                sign_in_button.place_forget()
                manage_account_button.place(x=270, y=650, width=120, height=40)
            except Exception:
                pass
        else:
            current_user_email = None

mainpage.mainloop()