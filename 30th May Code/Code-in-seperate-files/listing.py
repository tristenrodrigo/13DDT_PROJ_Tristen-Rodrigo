from tkinter import Label, Toplevel
from main import mainpage

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