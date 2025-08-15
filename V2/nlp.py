from fisf2.base import mainpage, conn, cursor
from tkinter import Label, Toplevel, Entry, filedialog, messagebox, StringVar, OptionMenu
from PIL import Image, ImageTk

def new_listing_page():
    new_listing_window = Toplevel(mainpage)
    new_listing_window.title("New Listing")
    new_listing_window.geometry("400x700")
    new_listing_window.config(bg="white")

    header = Label(new_listing_window, text="New Listing", font=("Lora", 24))
    header.config(bg="#4F6F52", fg="white")
    header.place(x=10, y=10, width=380, height=50)

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
    image_upload_button.place(x=200, y=70, width=180, height=30)
    image_upload_button.bind("<Button-1>", lambda event: upload_image())


    item_name_label = Label(new_listing_window, text="Item Name:", font=("Lora", 12), bg="white", fg="black")
    item_name_label.place(x=10, y=260, width=180, height=30)
    item_name_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")
    item_name_entry.place(x=200, y=260, width=180, height=30)

    item_description_label = Label(new_listing_window, text="Item Description:", font=("Lora", 12), bg="white", fg="black")
    item_description_label.place(x=10, y=300, width=180, height=30)
    item_description_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")
    item_description_entry.place(x=200, y=300, width=180, height=30)

    #Options for Item Category
    category_label = Label(new_listing_window, text="Item Category:", font=("Lora", 12), bg="white", fg="black")
    category_label.place(x=10, y=340, width=180, height=30)
    category_options = ["Clothes", "Shoes", "Accessories"]
    category_var = StringVar(new_listing_window)
    if category_options:
        category_var.set(category_options[0])
    else:
        category_var.set("Default")

    #Dropdown Menu for Item Category
    category_dropdown = OptionMenu(new_listing_window, text="Item Category:", font=("Lora", 12), bg="white", fg="black")
    category_dropdown.config(bg='white', fg="black")
    category_dropdown.place(x=200, y=340, width=180, height=30)
    category_dropdown['menu'].delete(0, 'end')  # Clear existing options
    for option in category_options:
        category_dropdown['menu'].add_command(label=option, command=lambda value=option: category_var.set(value))
    category_dropdown.config(variable=category_var)
    
    def save_listing():
        name = item_name_entry.get()
        description = item_description_entry.get()
        img_path = image_path["path"]
        if not name:
            messagebox.showwarning("Missing Name", "Please enter an item name.")
            return
        cursor.execute(
            'INSERT INTO listings (name, description, image_path) VALUES (?, ?, ?)',
            (name, description, img_path)
        )
        conn.commit()
        messagebox.showinfo("Info", "Listing saved successfully!")
        new_listing_window.destroy()

    publish_listing_button = Label(new_listing_window, text="Publish Listing", font=("Lora", 12), bg="#809D3C", fg="white")
    publish_listing_button.place(x=10, y=350, width=370, height=40)
    publish_listing_button.bind("<Button-1>", lambda event: save_listing())