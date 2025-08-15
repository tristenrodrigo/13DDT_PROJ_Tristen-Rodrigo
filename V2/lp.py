from fisf2.base import mainpage, cursor
from PIL import Image, ImageTk
from tkinter import Label, Toplevel

def listing_page():
    listing_window = Toplevel(mainpage)
    listing_window.title("Listing Page")
    listing_window.geometry("400x700")
    listing_window.config(bg="white")

    # Example: fetch the latest listing for demonstration
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