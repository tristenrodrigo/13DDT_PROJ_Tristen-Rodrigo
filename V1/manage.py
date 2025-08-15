from tkinter import Toplevel, Label, messagebox
import fisf1.shared as shared

def manage_account_page():
    mainpage = shared.mainpage
    cursor = shared.cursor
    current_user_email = shared.current_user_email

    manage_account_window = Toplevel(mainpage)
    manage_account_window.title("Manage Account")
    manage_account_window.geometry("400x700")
    manage_account_window.config(bg="white")

    header = Label(manage_account_window, text="Manage Account", font=("Lora", 24), bg="#4F6F52", fg="white")
    header.place(x=0, y=0, width=400, height=50)

    # Fetch user data from the database
    user_info = None
    if current_user_email:
        cursor.execute("SELECT first_name, last_name, email, gender, clothing_size, shoe_size FROM users WHERE email=?", (current_user_email,))
        user_info = cursor.fetchone()

    user_info_label = Label(manage_account_window, text="User Information", font=("Lora", 18), bg="white", fg="black")
    user_info_label.place(x=10, y=260, width=180, height=30)
    if user_info:
        info_text = f"Name: {user_info[0]} {user_info[1]}\nEmail: {user_info[2]}\nGender: {user_info[3]}\nClothing Size: {user_info[4]}\nShoe Size: {user_info[5]}"
    else:
        info_text = "No user info found."

    user_info_text = Label(manage_account_window, text=info_text, font=("Lora", 12), bg="white", fg="black", justify="left", anchor="nw")
    user_info_text.place(x=10, y=300, width=380, height=100)

    back_button = Label(manage_account_window, text="Back to Main Page", font=("Lora", 12), bg="#809D3C", fg="white")
    back_button.place(x=10, y=650, width=370, height=40)
    
    def handle_back(event):
        shared.current_user_email = None
        manage_account_window.destroy()
        shared.mainpage.deiconify()
        shared.update_mainpage_buttons()

    back_button.bind("<Button-1>", handle_back)