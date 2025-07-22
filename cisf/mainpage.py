from tkinter import Tk, Label, Toplevel, Entry
import cisf.shared as shared
from cisf.listings import listing_page

def launch_mainpage():
    shared.mainpage = Tk()
    mainpage = shared.mainpage
    mainpage.title("Loopwear")
    mainpage.geometry("400x700")
    mainpage.config(bg="white")

    mainpage.grid_columnconfigure(0, weight=1)
    header = Label(mainpage, text="Loopwear", font=("Lora", 24), bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=60)

    header_bar = Label(mainpage, bg='#809D3C')
    header_bar.place(x=0, y=60, width=400, height=40)

    # Search Bar
    search_bar = Entry(mainpage, font=("Lora", 12), bg="white", fg="black")
    search_bar.place(x=10, y=70, width=250, height=20)

    # Create Search Button
    search_button = Label(mainpage, text="Search", font=("Lora", 12), bg="#809D3C", fg="white")
    search_button.place(x=270, y=70, width=120, height=20)

    # Display listings based on category
    def display_category_listings(search_term=None):
        cursor = shared.cursor
        for widget in mainpage.winfo_children():
            if getattr(widget, "is_listing_label", False):
                widget.destroy()

        categories = [("Clothes", 180), ("Shoes", 360), ("Accessories", 540)]
        for category, y_fixed in categories:
            if search_term:
                cursor.execute(
                    "SELECT id, name, image_path FROM listings WHERE category=? AND name LIKE ?",
                    (category, f"%{search_term}%")
                )
            else:
                cursor.execute(
                    "SELECT id, name, image_path FROM listings WHERE category=?",
                    (category,)
                )
            listings = cursor.fetchall()
            x_offset = 10
            for listing in listings:
                img_label = Label(mainpage, text=listing[1], font=("Lora", 12), bg="black", fg="white")
                img_label.place(x=x_offset, y=y_fixed, width=100, height=100)
                img_label.is_listing_label = True
                img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), mainpage.withdraw()))
                x_offset += 120

    # Clothes Page
    def clothes_page():
        clothes_window = Toplevel(shared.mainpage)
        clothes_window.title("Clothes")
        clothes_window.geometry("400x700")
        clothes_window.config(bg="white")

        header = Label(clothes_window, text="Clothes", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        # Back Button
        back_button = Label(clothes_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
        back_button.place(x=10, y=650, width=370, height=40)
        back_button.bind("<Button-1>", lambda event: (clothes_window.destroy(), shared.mainpage.deiconify()))

        # Display Clothes Listings
        cursor = shared.cursor
        cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Clothes'")
        listings = cursor.fetchall()
        x_offset = 10
        y_fixed = 70
        for listing in listings:
            img_label = Label(clothes_window, text=listing[1], font=("Lora", 12), bg="black", fg="white")
            img_label.place(x=x_offset, y=y_fixed, width=100, height=100)
            img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), clothes_window.withdraw()))
            x_offset += 120

    # Creating Clothes Header
    clothes_header = Label(mainpage, text="Clothes", font=("Lora", 18), bg="#5D8736", fg="white")
    clothes_header.place(x=10, y=120, width=180, height=40)
    clothes_header.bind("<Button-1>", lambda event: (clothes_page(), mainpage.withdraw()))

    # Shoes Page
    def shoes_page():
        shoes_window = Toplevel(shared.mainpage)
        shoes_window.title("Shoes")
        shoes_window.geometry("400x700")
        shoes_window.config(bg="white")

        header = Label(shoes_window, text="Shoes", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        back_button = Label(shoes_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
        back_button.place(x=10, y=650, width=370, height=40)
        back_button.bind("<Button-1>", lambda event: (shoes_window.destroy(), shared.mainpage.deiconify()))

        # Display Shoes Listings
        cursor = shared.cursor
        cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Shoes'")
        listings = cursor.fetchall()
        x_offset = 10
        y_fixed = 70
        for listing in listings:
            img_label = Label(shoes_window, text=listing[1], font=("Lora", 12), bg="black", fg="white")
            img_label.place(x=x_offset, y=y_fixed, width=100, height=100)
            img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), shoes_window.withdraw()))
            x_offset += 120

    # Creating Shoes Header
    shoes_header = Label(mainpage, text="Shoes", font=("Lora", 18), bg="#5D8736", fg="white")
    shoes_header.place(x=10, y=300, width=180, height=40)
    shoes_header.bind("<Button-1>", lambda event: (shoes_page(), mainpage.withdraw()))

    # Accessories Page
    def accessories_page():
        accessories_window = Toplevel(shared.mainpage)
        accessories_window.title("Accessories")
        accessories_window.geometry("400x700")
        accessories_window.config(bg="white")

        header = Label(accessories_window, text="Accessories", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        back_button = Label(accessories_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
        back_button.place(x=10, y=650, width=370, height=40)
        back_button.bind("<Button-1>", lambda event: (accessories_window.destroy(), shared.mainpage.deiconify()))

        # Display Accessories Listings
        cursor = shared.cursor
        cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Accessories'")
        listings = cursor.fetchall()
        x_offset = 10
        y_fixed = 70
        for listing in listings:
            img_label = Label(accessories_window, text=listing[1], font=("Lora", 12), bg="black", fg="white")
            img_label.place(x=x_offset, y=y_fixed, width=100, height=100)
            img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), accessories_window.withdraw()))
            x_offset += 120

    # Creating Accessories Header
    accessories_header = Label(mainpage, text="Accessories", font=("Lora", 18), bg="#5D8736", fg="white")
    accessories_header.place(x=10, y=480, width=180, height=40)
    accessories_header.bind("<Button-1>", lambda event: (accessories_page(), mainpage.withdraw()))

    # Sign In Button
    sign_in_button = Label(mainpage, text="Sign In", font=("Lora", 12), bg="#5D8736", fg="white")
    sign_in_button.place(x=270, y=650, width=120, height=40)
    def open_sign_in(event):
        from cisf.signin import sign_in_page
        sign_in_page()
        mainpage.withdraw()
    sign_in_button.bind("<Button-1>", open_sign_in)

    # Manage Account Button
    manage_account_button = Label(mainpage, text="Manage Account", font=("Lora", 12), bg="#5D8736", fg="white")
    manage_account_button.place(x=270, y=650, width=120, height=40)
    def open_manage_account(event):
        from cisf.manage import manage_account_page
        manage_account_page()
        mainpage.withdraw()
    manage_account_button.bind("<Button-1>", open_manage_account)

    # New Listing Button
    new_listing_button = Label(mainpage, text="Create New Listing", font=("Lora", 12), bg="#809D3C", fg="white")
    new_listing_button.place(x=10, y=650, width=180, height=40)
    def open_new_listing(event):
        from cisf.listings import new_listing_page
        new_listing_page()
        mainpage.withdraw()
    new_listing_button.bind("<Button-1>", open_new_listing)

    def update_buttons():
        if shared.current_user_email:
            sign_in_button.place_forget()
            manage_account_button.place(x=270, y=650, width=180, height=40)
        else:
            manage_account_button.place_forget()
            sign_in_button.place(x=270, y=650, width=120, height=40)

    # Call this function whenever the login state changes
    update_buttons()
    shared.update_mainpage_buttons = update_buttons

    # Show listings when the app opens
    display_category_listings()

    # Search functionality
    def search_and_open_listing(event):
        cursor = shared.cursor
        search_term = search_bar.get()
        cursor.execute(
            "SELECT id FROM listings WHERE name LIKE ?",
            (f"%{search_term}%",)
        )
        results = cursor.fetchall()
        if len(results) == 1:
            listing_page(results[0][0])
        else:
            display_category_listings(search_term)

    search_button.bind("<Button-1>", search_and_open_listing)

    mainpage.mainloop()

def display_category_listings():
    cursor = shared.cursor
    mainpage = shared.mainpage

    for widget in mainpage.winfo_children():
        if getattr(widget, "is_listing_label", False):
            widget.destroy()

    # Clothes
    cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Clothes'")
    clothes_listings = cursor.fetchall()
    x_offset = 120
    y_fixed = 180
    for listing in clothes_listings:
        img_label = Label(mainpage, text=listing[1], font=("Lora", 12), bg="black", fg="white")
        img_label.place(x=x_offset, y=y_fixed, width=100, height=100)
        img_label.is_listing_label = True
        img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), mainpage.withdraw()))
        x_offset += 120

    # Shoes
    cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Shoes'")
    shoes_listings = cursor.fetchall()
    x_offset = 120
    y_fixed = 360
    for listing in shoes_listings:
        img_label = Label(mainpage, text=listing[1], font=("Lora", 12), bg="black", fg="white")
        img_label.place(x=x_offset, y=y_fixed, width=100, height=100)
        img_label.is_listing_label = True
        img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), mainpage.withdraw()))
        x_offset += 120

    # Accessories
    cursor.execute("SELECT id, name, image_path FROM listings WHERE category='Accessories'")
    accessories_listings = cursor.fetchall()
    x_offset = 120
    y_fixed = 540
    for listing in accessories_listings:
        img_label = Label(mainpage, text=listing[1], font=("Lora", 12), bg="black", fg="white")
        img_label.place(x=x_offset, y=y_fixed, width=100, height=100)
        img_label.is_listing_label = True
        img_label.bind("<Button-1>", lambda event, listing_id=listing[0]: (listing_page(listing_id), mainpage.withdraw()))
        x_offset += 120