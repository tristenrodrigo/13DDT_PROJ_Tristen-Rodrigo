from tkinter import Toplevel, Label, Entry, StringVar, OptionMenu, filedialog, messagebox
from PIL import Image, ImageTk

class ListingsPage:
    def __init__(self, shared):
        self.shared = shared

    def new_listing_page(self):
        mainpage = self.shared.mainpage
        cursor = self.shared.cursor
        conn = self.shared.conn

        new_listing_window = Toplevel(mainpage)
        new_listing_window.title("New Listing")
        new_listing_window.geometry("400x700")
        new_listing_window.resizable(False, False)
        
        new_listing_window.config(bg="white")

        header = Label(new_listing_window, text="New Listing", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        uploaded_image_label = Label(new_listing_window, bg="white")
        uploaded_image_label.place(x=10, y=70, width=180, height=180)
        image_path = {"path": None}

        def upload_image():
            file_path = filedialog.askopenfilename(title='Select an Image',filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*")])
            if file_path:
                try:
                    img = Image.open(file_path)
                    img = img.resize((180, 180))
                    photo = ImageTk.PhotoImage(img)
                    uploaded_image_label.config(image=photo)
                    uploaded_image_label.image = photo
                    image_path["path"] = file_path
                except Exception as e:
                    messagebox.showerror("Error", f"Could not open image file.\n{e}")

        image_upload_button = Label(new_listing_window, text="Upload Image", font=("Lora", 12), bg="#809D3C", fg="black")
        image_upload_button.place(x=110, y=70, width=180, height=30)
        image_upload_button.bind("<Button-1>", lambda event: upload_image())

        item_name_label = Label(new_listing_window, text="Item Name:", font=("Lora", 12), bg="white", fg="black")
        item_name_label.place(x=10, y=110, width=70, height=30)
        item_name_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")
        item_name_entry.place(x=200, y=110, width=180, height=30)

        item_description_label = Label(new_listing_window, text="Item Description:", font=("Lora", 12), bg="white", fg="black")
        item_description_label.place(x=10, y=160, width=100, height=30)

        item_description_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")
        item_description_entry.place(x=200, y=160, width=180, height=50)

        category_dropdown_label = Label(new_listing_window, text="Category:", font=("Lora", 12), bg="white", fg="black")
        category_dropdown_label.place(x=10, y=360, width=100, height= 30)
        category_dropdown_label.config(bg="white", fg="black")
        
        # Category dropdown and extra options
        category_options = ["Clothes", "Shoes", "Accessories"]
        category_var = StringVar(new_listing_window)
        category_var.set("Select Category")

        # Extra option widgets
        clothes_size_label = Label(new_listing_window, text="Clothing Size:", font=("Lora", 12), bg="white", fg="black")
        clothes_size_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")

        shoes_size_label = Label(new_listing_window, text="Shoe Size:", font=("Lora", 12), bg="white", fg="black")
        shoes_size_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")

        accessory_type_label = Label(new_listing_window, text="Accessory Type:", font=("Lora", 12), bg="white", fg="black")
        accessory_type_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")

        def show_extra_options(selected_category=None):
            clothes_size_label.place_forget()
            clothes_size_entry.place_forget()
            shoes_size_label.place_forget()
            shoes_size_entry.place_forget()
            accessory_type_label.place_forget()
            accessory_type_entry.place_forget()

            category = selected_category if selected_category else category_var.get()

            if category == "Clothes":
                clothes_size_label.place(x=10, y=400, width=120, height=30)
                clothes_size_entry.place(x=140, y=400, width=120, height=30)
            elif category == "Shoes":
                shoes_size_label.place(x=10, y=400, width=120, height=30)
                shoes_size_entry.place(x=140, y=400, width=120, height=30)
            elif category == "Accessories":
                accessory_type_label.place(x=10, y=400, width=120, height=30)
                accessory_type_entry.place(x=140, y=400, width=120, height=30)

        category_dropdown = OptionMenu(
            new_listing_window, category_var, *category_options, command=show_extra_options
        )
        category_dropdown.config(bg='white', fg="black")
        category_dropdown.place(x=120, y=360, width=120, height=30)

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

        back_button = Label(new_listing_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
        back_button.place(x=10, y=650, width=370, height=40)
        back_button.bind("<Button-1>", lambda event: (new_listing_window.destroy(), mainpage.deiconify()))

    def listing_page(self, listing_id=None):
        mainpage = self.shared.mainpage
        cursor = self.shared.cursor
        conn = self.shared.conn

        listing_window = Toplevel(mainpage)
        listing_window.title("Listing Page")
        listing_window.geometry("400x700")
        listing_window.resizable(False, False)
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

        img_label = Label(listing_window, bg="white")
        img_label.place(x=200, y=70, width=180, height=180)
        if listing and listing[2]:
            try:
                img = Image.open(listing[2])
                img = img.resize((180, 180))
                photo = ImageTk.PhotoImage(img)
                img_label.config(image=photo)
                img_label.image = photo
            except Exception:
                img_label.config(text="Image not found", fg="red")

        img_label.bind(
            "<Button-1>",
            lambda event, listing_id=listing[0]: (
                ListingsPage(self.shared).listing_page(listing_id),
                mainpage.withdraw()
            )
        )