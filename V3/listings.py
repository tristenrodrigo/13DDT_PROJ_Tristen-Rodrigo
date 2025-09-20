from tkinter import Toplevel, Label, Entry, StringVar, OptionMenu, filedialog, messagebox, Message, Text
from PIL import Image, ImageTk
import os
import shutil

class ListingsPage:
    def __init__(self, shared):
        self.shared = shared  # Shared state for accessing main window, db, etc.

    def new_listing_page(self):
        mainpage = self.shared.mainpage
        cursor = self.shared.cursor
        conn = self.shared.conn

        # Create the New Listing window
        new_listing_window = Toplevel(mainpage)
        new_listing_window.title("New Listing")
        new_listing_window.geometry("400x700")
        new_listing_window.resizable(False, False)
        new_listing_window.config(bg="white")

        # Header
        header = Label(new_listing_window, text="New Listing", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        # --- Image upload section ---
        uploaded_image_label = Label(new_listing_window, bg="white", relief="groove")
        uploaded_image_label.place(x=30, y=70, width=120, height=120)
        image_path = {"path": None}

        def upload_image():
            file_path = filedialog.askopenfilename(
                filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
            )
            if file_path:
                try:
                    img = Image.open(file_path)
                    img = img.resize((120, 120))
                    photo = ImageTk.PhotoImage(img)
                    uploaded_image_label.config(image=photo)
                    uploaded_image_label.image = photo

                    images_dir = os.path.join(os.path.dirname(__file__), "images")
                    os.makedirs(images_dir, exist_ok=True)
                    filename = os.path.basename(file_path)
                    save_path = os.path.join(images_dir, filename)
                    shutil.copy(file_path, save_path)
                    image_path["path"] = save_path
                except Exception as e:
                    messagebox.showerror("Error", f"Could not open image file.\n{e}")

        image_upload_button = Label(new_listing_window, text="Upload Image", font=("Lora", 12), bg="#809D3C", fg="white", cursor="hand2")
        image_upload_button.place(x=170, y=110, width=190, height=40)
        image_upload_button.bind("<Button-1>", lambda event: upload_image())

        # --- Category dropdown ---
        category_label = Label(new_listing_window, text="Category:", font=("Lora", 12), bg="white", fg="black")
        category_label.place(x=30, y=210, width=120, height=30)
        category_options = ["Clothes", "Shoes", "Accessories"]
        category_var = StringVar(new_listing_window)
        category_var.set(category_options[0])
        category_dropdown = OptionMenu(new_listing_window, category_var, *category_options)
        category_dropdown.config(bg='white', fg="black")
        category_dropdown.place(x=170, y=210, width=190, height=30)

        # --- Extra fields for each category ---
        clothes_size_label = Label(new_listing_window, text="Clothing Size:", font=("Lora", 12), bg="white", fg="black")
        clothes_size_options = ["XS", "S", "M", "L", "XL", "XXL"]
        clothes_size_var = StringVar(new_listing_window)
        clothes_size_var.set(clothes_size_options[0])
        clothes_size_dropdown = OptionMenu(new_listing_window, clothes_size_var, *clothes_size_options)

        shoes_size_label = Label(new_listing_window, text="Shoe Size:", font=("Lora", 12), bg="white", fg="black")
        shoes_size_options = [str(size) for size in range(5, 14)]
        shoes_size_var = StringVar(new_listing_window)
        shoes_size_var.set(shoes_size_options[0])
        shoes_size_dropdown = OptionMenu(new_listing_window, shoes_size_var, *shoes_size_options)

        accessory_type_label = Label(new_listing_window, text="Accessory Type:", font=("Lora", 12), bg="white", fg="black")
        accessory_type_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")

        def show_extra_options(*args):
            clothes_size_label.place_forget()
            clothes_size_dropdown.place_forget()
            shoes_size_label.place_forget()
            shoes_size_dropdown.place_forget()
            accessory_type_label.place_forget()
            accessory_type_entry.place_forget()

            category = category_var.get()
            if category == "Clothes":
                clothes_size_label.place(x=30, y=250, width=120, height=30)
                clothes_size_dropdown.place(x=170, y=250, width=190, height=30)
                clothes_size_dropdown.config(bg='white', fg="black")
            elif category == "Shoes":
                shoes_size_label.place(x=30, y=250, width=120, height=30)
                shoes_size_dropdown.place(x=170, y=250, width=190, height=30)
                shoes_size_dropdown.config(bg='white', fg="black")
            elif category == "Accessories":
                accessory_type_label.place(x=30, y=250, width=120, height=30)
                accessory_type_entry.place(x=170, y=250, width=190, height=30)

        category_var.trace_add("write", show_extra_options)
        show_extra_options()

        # --- Item Name ---
        item_name_label = Label(new_listing_window, text="Item Name:", font=("Lora", 12), bg="white", fg="black")
        item_name_label.place(x=30, y=300, width=120, height=30)
        item_name_entry = Entry(new_listing_window, font=("Lora", 12), bg='white', fg="black")
        item_name_entry.place(x=170, y=300, width=190, height=30)

        # --- Item Description ---
        item_description_label = Label(new_listing_window, text="Description:", font=("Lora", 12), bg="white", fg="black")
        item_description_label.place(x=30, y=350, width=120, height=30)
        item_description_entry = Text(new_listing_window, font=("Lora", 12), bg='white', fg="black", wrap="word")
        item_description_entry.place(x=170, y=350, width=190, height=80)

        # --- Contact Visibility dropdown (placed above Publish button) ---
        contact_visibility_label = Label(new_listing_window, text="Show to buyers:", font=("Lora", 12), bg="white", fg="black")
        contact_visibility_label.place(x=30, y=470, width=120, height=30)
        contact_visibility_options = ["Email", "Phone", "Both"]
        contact_visibility_var = StringVar(new_listing_window)
        contact_visibility_var.set(contact_visibility_options[0])
        contact_visibility_dropdown = OptionMenu(new_listing_window, contact_visibility_var, *contact_visibility_options)
        contact_visibility_dropdown.config(bg='white', fg="black")
        contact_visibility_dropdown.place(x=170, y=470, width=190, height=30)

        # --- Publish Listing Button ---
        publish_listing_button = Label(new_listing_window, text="Publish Listing", font=("Lora", 12), bg="#809D3C", fg="white", cursor="hand2")
        publish_listing_button.place(x=30, y=520, width=330, height=40)
        publish_listing_button.bind("<Button-1>", lambda event: save_listing())

        # --- Save listing to database ---
        def save_listing():
            name = item_name_entry.get()
            description = item_description_entry.get("1.0", "end-1c")
            img_path = image_path["path"]
            category = category_var.get()
            extra1 = None
            seller_email = getattr(self.shared, 'current_user_email', None)
            contact_visibility = contact_visibility_var.get()
            if not name:
                messagebox.showwarning("Missing Name", "Please enter an item name.")
                return
            if category == "Clothes":
                extra1 = clothes_size_var.get()
            elif category == "Shoes":
                extra1 = shoes_size_var.get()
            elif category == "Accessories":
                extra1 = accessory_type_entry.get()
            cursor.execute(
                'INSERT INTO listings (name, description, image_path, category, seller_email, contact_visibility) VALUES (?, ?, ?, ?, ?, ?)',
                (name, description, img_path, category, seller_email, contact_visibility)
            )
            conn.commit()
            messagebox.showinfo("Info", "Listing saved successfully!")
            new_listing_window.destroy()
            mainpage.deiconify()

        # --- Back Button ---
        back_button = Label(new_listing_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white", cursor="hand2")
        back_button.place(x=30, y=580, width=330, height=40)
        back_button.bind("<Button-1>", lambda event: (new_listing_window.destroy(), mainpage.deiconify()))

    def listing_page(self, listing_id=None):
        mainpage = self.shared.mainpage
        cursor = self.shared.cursor
        conn = self.shared.conn

        # Create the Listing Details window
        listing_window = Toplevel(mainpage)
        listing_window.title("Listing Page")
        listing_window.geometry("400x700")
        listing_window.resizable(False, False)
        listing_window.config(bg="white")

        # Fetch listing info, including seller_email
        if listing_id:
            cursor.execute("SELECT name, description, image_path, category, seller_email FROM listings WHERE id=?", (listing_id,))
        else:
            cursor.execute("SELECT name, description, image_path, category, seller_email FROM listings ORDER BY id DESC LIMIT 1")
        listing = cursor.fetchone()

        # --- Header ---
        header = Label(listing_window, text=listing[0] if listing else "Listing", font=("Lora", 24, "bold"), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=60)

        # --- Image Section ---
        image_frame = Label(listing_window, bg="white", relief="groove")
        image_frame.place(x=140, y=70, width=120, height=120)
        if listing and listing[2]:
            try:
                img = Image.open(listing[2])
                img = img.resize((120, 120))
                photo = ImageTk.PhotoImage(img)
                image_frame.config(image=photo)
                image_frame.image = photo
            except Exception:
                image_frame.config(text="Image not found", fg="red", font=("Lora", 10))
        else:
            image_frame.config(text="No image", fg="gray", font=("Lora", 10))

        # --- Category ---
        category_label = Label(listing_window, text=f"Category: {listing[3] if listing else ''}", font=("Lora", 12, "bold"), bg="white", fg="#809D3C")
        category_label.place(x=10, y=200, width=380, height=30)

        # --- Description Section ---
        description_header = Label(listing_window, text="Description", font=("Lora", 14, "bold"), bg="white", fg="#4F6F52")
        description_header.place(x=10, y=240, width=380, height=30)
        description_text = Message(listing_window, text=listing[1] if listing else "", font=("Lora", 12), bg="white", fg="black", width=360)
        description_text.place(x=20, y=280, width=360, height=80)

        # --- Seller Info Section ---
        seller_y = 370
        if listing and listing[4]:
            seller_email = listing[4]
            contact_visibility = listing[5] if len(listing) > 5 else "Email"
            cursor.execute("SELECT first_name, last_name, phone FROM users WHERE email=?", (seller_email,))
            seller = cursor.fetchone()
            seller_name = f"{seller[0]} {seller[1]}" if seller else "Unknown"
            seller_phone = seller[2] if seller else "Unknown"
            seller_email_display = seller_email if seller else "Unknown"

            seller_header = Label(listing_window, text="Seller Information", font=("Lora", 14, "bold"), bg="white", fg="#4F6F52")
            seller_header.place(x=10, y=seller_y, width=380, height=30)
            seller_name_label = Label(listing_window, text=f"Name: {seller_name}", font=("Lora", 12), bg="white", fg="black")
            seller_name_label.place(x=10, y=seller_y+35, width=380, height=25)

            # Show contact info based on visibility setting
            contact_y = seller_y + 65
            if contact_visibility == "Email":
                Label(listing_window, text=f"Email: {seller_email_display}", font=("Lora", 12), bg="white", fg="black").place(x=10, y=contact_y, width=380, height=25)
            elif contact_visibility == "Phone":
                Label(listing_window, text=f"Phone: {seller_phone}", font=("Lora", 12), bg="white", fg="black").place(x=10, y=contact_y, width=380, height=25)
            elif contact_visibility == "Both":
                Label(listing_window, text=f"Email: {seller_email_display}", font=("Lora", 12), bg="white", fg="black").place(x=10, y=contact_y, width=380, height=25)
                Label(listing_window, text=f"Phone: {seller_phone}", font=("Lora", 12), bg="white", fg="black").place(x=10, y=contact_y+30, width=380, height=25)
        # If "None", show nothing extra

        # --- Back Button ---
        back_button = Label(listing_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
        back_button.place(x=10, y=650, width=370, height=40)
        back_button.bind("<Button-1>", lambda event: (listing_window.destroy(), mainpage.deiconify()))