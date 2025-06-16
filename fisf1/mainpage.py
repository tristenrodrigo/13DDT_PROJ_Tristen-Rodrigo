from tkinter import Tk, Label, Entry, messagebox
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
    manage_account_button.place(x=10, y=650, width=180, height=40)
    def open_manage_account(event):
        from fisf1.manage import manage_account_page
        manage_account_page()
        mainpage.withdraw()
    manage_account_button.bind("<Button-1>", open_manage_account)

    # New Listing Button
    new_listing_button = Label(mainpage, text="Create New Listing", font=("Lora", 12), bg="#809D3C", fg="white")
    new_listing_button.place(x=10, y=600, width=180, height=40)
    def open_new_listing(event):
        from fisf1.newlisting import new_listing_page
        new_listing_page()
        mainpage.withdraw()
    new_listing_button.bind("<Button-1>", open_new_listing)

    # Example: Add more navigation as needed

    mainpage.mainloop()