from tkinter import Tk, Label, Entry, messagebox
from si import sign_in_page
import sqlite3

def mainpage():
    global mainpage, manage_account_button
    mainpage = Tk()
    mainpage.title("Loopwear")
    mainpage.geometry("400x700")
    mainpage.config(bg="white")

    # Creating Header
    mainpage.grid_columnconfigure(0, weight=1)
    header = Label(mainpage, text="Loopwear", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=60)

    # Creating Header Bar
    header_bar = Label(mainpage)
    header_bar.config(bg='#809D3C')
    header_bar.place(x=0, y=60, width=400, height=40)

    # Creating Sign Up Button (placed on top of the header bar)
    global sign_in_button
    sign_in_button = Label(mainpage, text="Sign In", font=("Lora", 12), bg="#5D8736", fg="white", anchor="center")
    sign_in_button.place(x=270, y=650, width=120, height=40)
    sign_in_button.bind("<Button-1>", open_sign_in_close_main)

    # Creating Manage Account Button (initially hidden)
    manage_account_button = Label(mainpage, text="Manage Account", font=("Lora", 12), bg="#5D8736", fg="white", anchor="center")
    manage_account_button.place_forget()

    # Search Bar
    search_bar = Entry(mainpage, font=("Lora", 12), bg="white", fg="black")
    search_bar.place(x=10, y=70, width=250, height=20)

    # Creating Search Button
    search_button = Label(mainpage, text="Search", font=("Lora", 12), bg="#809D3C", fg="white")
    search_button.place(x=270, y=70, width=120, height=20)
    search_button.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Search functionality is under construction."))

    # New Listing Button
    from new_listing import new_listing_page
    new_listing_button = Label(mainpage, text="Create New Listing", font=("Lora", 12), bg="#809D3C", fg="white", anchor="center")
    new_listing_button.place(x=10, y=650, width=180, height=40)
    new_listing_button.bind("<Button-1>", lambda event: new_listing_page())

    # Creating Clothes Header
    clothes_header = Label(mainpage, text="Clothes", font=("Lora", 18), bg="#5D8736", fg="white")
    clothes_header.place(x=10, y=120, width=180, height=40)
    clothes_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Clothes section is under construction."))

    # listing Image Test
    from listing import listing_page
    clothes_listing_image1 = Label(mainpage, text="Listing Image", font=("Lora", 12), bg="black", fg="black")
    clothes_listing_image1.place(x=10, y=180, width=100, height=100)
    clothes_listing_image1.bind("<Button-1>", lambda event: (listing_page(), mainpage.withdraw()))

    # Creating Shoes Header
    shoes_header = Label(mainpage, text="Shoes", font=("Lora", 18), bg="#5D8736", fg="white")
    shoes_header.place(x=10, y=300, width=180, height=40)
    shoes_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Shoes section is under construction."))

    # listing Image Test
    clothes_listing_image2 = Label(mainpage, text="Listing Image", font=("Lora", 12), bg="black", fg="black")
    clothes_listing_image2.place(x=10, y=360, width=100, height=100)
    clothes_listing_image2.bind("<Button-1>", lambda event: (listing_page(), mainpage.withdraw()))

    # Creating Accessories Header
    accessories_header = Label(mainpage, text="Accessories", font=("Lora", 18), bg="#5D8736", fg="white")
    accessories_header.place(x=10, y=480, width=180, height=40)
    accessories_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Accessories section is under construction."))

    # listing Image Test
    clothes_listing_image3 = Label(mainpage, text="Listing Image", font=("Lora", 12), bg="black", fg="black")
    clothes_listing_image3.place(x=10, y=540, width=100, height=100)
    clothes_listing_image3.bind("<Button-1>", lambda event: (listing_page(), mainpage.withdraw()))

# Create/connect to the database
conn = sqlite3.connect('listings.db')
cursor = conn.cursor()

# Create the listings table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
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
    pass 

def update_mainpage_for_login():
    sign_in_button.place_forget()
    manage_account_button.place(x=270, y=650, width=120, height=40)

def open_sign_in_close_main(event):
    sign_in_page()
    mainpage.withdraw()

# Start the main loop
mainpage.mainloop()