from tkinter import Toplevel, Label, Entry, messagebox, StringVar, OptionMenu

class ManageAccountPage:
    def __init__(self, shared):
        self.shared = shared

    def manage_account_page(self):
        mainpage = self.shared.mainpage
        cursor = self.shared.cursor
        current_user_email = self.shared.current_user_email

        manage_account_window = Toplevel(mainpage)
        manage_account_window.title("Manage Account")
        manage_account_window.geometry("400x700")
        manage_account_window.resizable(False, False)
        manage_account_window.config(bg="white")

        header = Label(manage_account_window, text="Manage Account", font=("Lora", 24), bg="#4F6F52", fg="white")
        header.place(x=0, y=0, width=400, height=50)

        # Fetch user data from the database
        user_info = None
        if current_user_email:
            cursor.execute("SELECT first_name, last_name, email, gender, clothing_size, shoe_size FROM users WHERE email=?", (current_user_email,))
            user_info = cursor.fetchone()

        # User Info Section
        user_info_label = Label(
            manage_account_window,
            text="User Information",
            font=("Lora", 18, "bold"),
            bg="white",
            fg="#4F6F52"
        )
        user_info_label.place(x=10, y=120, width=380, height=40)

        if user_info:
            # Nicely formatted info with bold labels
            info_labels = ["Name:", "Email:", "Gender:", "Clothing Size:", "Shoe Size:"]
            info_values = [
                f"{user_info[0]} {user_info[1]}",
                user_info[2],
                user_info[3],
                user_info[4],
                user_info[5]
            ]
            y_start = 170
            for i, (label_text, value_text) in enumerate(zip(info_labels, info_values)):
                label = Label(
                    manage_account_window,
                    text=label_text,
                    font=("Lora", 12, "bold"),
                    bg="white",
                    fg="#333"
                )
                label.place(x=30, y=y_start + i*40, width=120, height=30)
                value = Label(
                    manage_account_window,
                    text=value_text,
                    font=("Lora", 12),
                    bg="white",
                    fg="#222"
                )
                value.place(x=160, y=y_start + i*40, width=220, height=30)
        else:
            info_text = "No user info found."
            user_info_text = Label(
                manage_account_window,
                text=info_text,
                font=("Lora", 12),
                bg="white",
                fg="red",
                justify="left",
                anchor="nw"
            )
            user_info_text.place(x=10, y=170, width=380, height=30)

        back_button = Label(manage_account_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
        back_button.place(x=205, y=600, width=185, height=40)
        
        def handle_back(event):
            manage_account_window.destroy()
            mainpage.deiconify()

        back_button.bind("<Button-1>", handle_back)

        def edit_account_page(self):
            mainpage = self.shared.mainpage
            cursor = self.shared.cursor
            conn = self.shared.conn
            current_user_email = self.shared.current_user_email

            edit_window = Toplevel(mainpage)
            edit_window.title("Edit Account")
            edit_window.geometry("400x700")
            edit_window.resizable(False, False)
            edit_window.config(bg="white")

            header = Label(edit_window, text="Edit Account", font=("Lora", 24), bg="#4F6F52", fg="white")
            header.place(x=0, y=0, width=400, height=50)

            # Fetch current user info
            cursor.execute("SELECT first_name, last_name, gender, clothing_size, shoe_size FROM users WHERE email=?", (current_user_email,))
            user_info = cursor.fetchone() if current_user_email else None

            # Entry fields
            first_name_entry = Entry(edit_window, font=("Lora", 12), bg="white", fg="black")
            last_name_entry = Entry(edit_window, font=("Lora", 12), bg="white", fg="black")

            # Dropdown options
            gender_options = ["Male", "Female", "Other"]
            clothing_size_options = ["XS", "S", "M", "L", "XL", "XXL"]
            shoe_size_options = [str(size) for size in range(5, 14)]

            # StringVars for dropdowns
            gender_var = StringVar(edit_window)
            clothing_size_var = StringVar(edit_window)
            shoe_size_var = StringVar(edit_window)

            # Pre-fill with current info
            if user_info:
                first_name_entry.insert(0, user_info[0])
                last_name_entry.insert(0, user_info[1])
                gender_var.set(user_info[2])
                clothing_size_var.set(user_info[3])
                shoe_size_var.set(user_info[4])
            else:
                gender_var.set(gender_options[0])
                clothing_size_var.set(clothing_size_options[0])
                shoe_size_var.set(shoe_size_options[0])

            Label(edit_window, text="First Name:", font=("Lora", 12), bg="white", fg="black").place(x=10, y=70, width=120, height=30)
            first_name_entry.place(x=140, y=70, width=200, height=30)
            Label(edit_window, text="Last Name:", font=("Lora", 12), bg="white", fg="black").place(x=10, y=120, width=120, height=30)
            last_name_entry.place(x=140, y=120, width=200, height=30)

            Label(edit_window, text="Gender:", font=("Lora", 12), bg="white", fg="black").place(x=10, y=170, width=120, height=30)
            gender_dropdown = OptionMenu(edit_window, gender_var, *gender_options)
            gender_dropdown.place(x=140, y=170, width=200, height=30)

            Label(edit_window, text="Clothing Size:", font=("Lora", 12), bg="white", fg="black").place(x=10, y=220, width=120, height=30)
            clothing_size_dropdown = OptionMenu(edit_window, clothing_size_var, *clothing_size_options)
            clothing_size_dropdown.place(x=140, y=220, width=200, height=30)

            Label(edit_window, text="Shoe Size:", font=("Lora", 12), bg="white", fg="black").place(x=10, y=270, width=120, height=30)
            shoe_size_dropdown = OptionMenu(edit_window, shoe_size_var, *shoe_size_options)
            shoe_size_dropdown.place(x=140, y=270, width=200, height=30)

            def save_changes(event):
                cursor.execute(
                    "UPDATE users SET first_name=?, last_name=?, gender=?, clothing_size=?, shoe_size=? WHERE email=?",
                    (
                        first_name_entry.get(),
                        last_name_entry.get(),
                        gender_var.get(),
                        clothing_size_var.get(),
                        shoe_size_var.get(),
                        current_user_email
                    )
                )
                conn.commit()
                messagebox.showinfo("Success", "Account updated successfully!")
                edit_window.destroy()
                mainpage.deiconify()

            save_button = Label(edit_window, text="Save Changes", font=("Lora", 12), bg="#809D3C", fg="white")
            save_button.place(x=10, y=320, width=370, height=40)
            save_button.bind("<Button-1>", save_changes)

            back_button = Label(edit_window, text="Back to Manage Account", font=("Lora", 12), bg="#809D3C", fg="white")
            back_button.place(x=10, y=650, width=370, height=40)
            back_button.bind("<Button-1>", lambda event: (edit_window.destroy(), mainpage.deiconify()))
    
        edit_button = Label(manage_account_window, text="Edit Account", font=("Lora", 12), bg="#809D3C", fg="white")
        edit_button.place(x=10, y=600, width=185, height=40)
        edit_button.bind("<Button-1>", lambda event: (manage_account_window.withdraw(), edit_account_page(self)))

        # Log Out Button
        def handle_logout(event):
            # Remove session file if it exists
            import os
            if os.path.exists("session.txt"):
                os.remove("session.txt")
            self.shared.current_user_email = None
            if hasattr(self.shared, "session_code"):
                del self.shared.session_code
            messagebox.showinfo("Logged Out", "You have been logged out.")
            manage_account_window.destroy()
            mainpage.deiconify()
            self.shared.update_mainpage_buttons()

        logout_button = Label(manage_account_window, text="Log Out", font=("Lora", 12), bg="#B22222", fg="white")
        logout_button.place(x=10, y=650, width=380, height=40)
        logout_button.bind("<Button-1>", handle_logout)