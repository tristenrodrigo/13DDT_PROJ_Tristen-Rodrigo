from tkinter import Label, Button, Toplevel, Entry, messagebox
from main import mainpage

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