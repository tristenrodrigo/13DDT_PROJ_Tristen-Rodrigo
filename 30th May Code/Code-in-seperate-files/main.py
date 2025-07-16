from tkinter import Tk, Label, Button, Entry, messagebox
from PIL import Image, ImageTk
from sign_in import sign_in_page
from listing import listing_page

mainpage = Tk()

#Creating title and main window
mainpage.title("Loopwear") 
mainpage.geometry("400x700")
mainpage.config(bg="white")

#Creating Header
mainpage.grid_columnconfigure(0, weight=1)
header = Label(mainpage, text="Loopwear", font=("Lora", 24))
header.config(bg="#4F6F52", fg="white")
header.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

#Creating Header Bar
header_bar = Label(mainpage)
header_bar.config(bg='#809D3C')
header_bar.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

def open_sign_in_close_main(event):
    sign_in_page()
    mainpage.withdraw()

#Creating Sign Up Button (placed on top of the header bar)
sign_in_button = Label(mainpage, text="Sign In", font=("Lora", 12), bg="#5D8736", fg="black", anchor="w")
sign_in_button.grid(row=10, column=1, sticky="w", padx=10, pady=10) 
sign_in_button.bind("<Button-1>", open_sign_in_close_main)

#Search Bar
search_bar = Entry(mainpage, font=("Lora", 12), bg="white", fg="black")
search_bar.grid(row=1, column=0, sticky="w", padx=5, pady=5)

#Creating Search Button
search_button = Label(mainpage, text="Search", font=("Lora", 12), bg="#809D3C", fg="white")
search_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)
search_button.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Search functionality is under construction."))

#New listing button
new_listing_button = Label(mainpage, text="Create New Listing",font=("Lora", 12), bg="#809D3C", fg="white", anchor="center")
new_listing_button.grid(row=10, column=0, sticky="s", padx=10, pady=10)
new_listing_button.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "New listing functionality is under construction."))

#Creating Clothes Header
clothes_header = Label(mainpage, text="Clothes", font=("Lora", 18), bg="#5D8736", fg="white")
clothes_header.grid(row=2, column=0, sticky="w", padx=5, pady=5)
clothes_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Clothes section is under construction."))

#Creating Shoes Header
shoes_header = Label(mainpage, text="Shoes", font=("Lora", 18), bg="#5D8736", fg="white")
shoes_header.grid(row=4, column=0, sticky="w", padx=5, pady=5)
shoes_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Shoes section is under construction."))

#Creating Accessories Header
accessories_header = Label(mainpage, text="Accessories", font=("Lora", 18), bg="#5D8736", fg="white")
accessories_header.grid(row=6, column=0, sticky="w", padx=5, pady=5)
accessories_header.bind("<Button-1>", lambda event: messagebox.showinfo("Info", "Accessories section is under construction."))
# Load and resize the image
original_image = Image.open("/Users/tristenrodrigo/Documents/School/13DDT/13DDT_PROJ_Tristen Rodrigo/Image/Shirt.png")
resized_image = original_image.resize((80, 80))
clothes_image = ImageTk.PhotoImage(resized_image)

#Clothes listing image button
clothes_listing_button = Button(mainpage, image=clothes_image, command=listing_page, bg="white")
clothes_listing_button.grid(row=3, column=0, sticky="w", padx=10, pady=10)

mainpage.mainloop()