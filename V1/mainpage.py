from tkinter import Tk, Label, Toplevel
import fisf1.shared as shared

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

    # Sign In Button
    sign_in_button = Label(mainpage, text="Sign In", font=("Lora", 12), bg="#5D8736", fg="white")
    sign_in_button.place(x=270, y=650, width=120, height=40)
    def open_sign_in(event):
        from fisf1.signin import sign_in_page
        sign_in_page()
        mainpage.withdraw()
    sign_in_button.bind("<Button-1>", open_sign_in)

    # Manage Account Button
    manage_account_button = Label(mainpage, text="Manage Account", font=("Lora", 12), bg="#5D8736", fg="white")
    manage_account_button.place(x=270, y=650, width=180, height=40)
    def open_manage_account(event):
        from fisf1.manage import manage_account_page
        manage_account_page()
        mainpage.withdraw()
    manage_account_button.bind("<Button-1>", open_manage_account)

    # New Listing Button
    new_listing_button = Label(mainpage, text="Create New Listing", font=("Lora", 12), bg="#809D3C", fg="white")
    new_listing_button.place(x=10, y=650, width=180, height=40)
    def open_new_listing(event):
        from fisf1.newlisting import new_listing_page
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
    shared.update_mainpage_buttons = update_buttons  # So other modules can call it

    mainpage.mainloop()