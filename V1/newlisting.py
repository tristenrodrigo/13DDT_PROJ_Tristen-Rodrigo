from tkinter import Toplevel, Label, Entry, StringVar, OptionMenu, filedialog, messagebox
from PIL import Image, ImageTk
import fisf1.shared as shared

def new_listing_page():
    mainpage = shared.mainpage
    cursor = shared.cursor
    conn = shared.conn

    new_listing_window = Toplevel(mainpage)
    new_listing_window.title("New Listing")
    new_listing_window.geometry("400x700")
    new_listing_window.config(bg="white")

    header = Label(new_listing_window, text="New Listing", font=("Lora", 24), bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    uploaded_image_label = Label(new_listing_window, bg="white")
    uploaded_image_label.place(x=10, y=70, width=180, height=180)
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
                image_path["path"] = file_path
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

    publish_listing_button = Label(new_listing_window, text="Publish Listing", font=("Lora", 12), bg="#809D3C", fg="white")
    publish_listing_button.place(x=10, y=400, width=370, height=40)
    publish_listing_button.bind("<Button-1>", lambda event: save_listing())