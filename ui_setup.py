# modulo ui_setup.py
from tkinter import *
from tkinter import messagebox

class UI_Setup:
    def __init__(self, password_manager):
        self.password_manager = password_manager
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
        self.window.resizable(False, False)

        # Canvas
        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0, columnspan=3)

        # Website
        self.label_website = Label(text="Website: ", font=("Courier", 8))
        self.label_website.grid(column=0, row=1, sticky="e")
        self.input_website = Entry(width=35)
        self.input_website.grid(column=1, row=1, sticky="w", columnspan=2)
        self.input_website.focus()

        # Email/Username
        self.label_email_username = Label(text="Email/Username: ", font=("Courier", 8))
        self.label_email_username.grid(column=0, row=2, sticky="e")
        self.input_email_username = Entry(width=35)
        self.input_email_username.grid(column=1, row=2, sticky="w", columnspan=2)
        self.input_email_username.insert(0, "carlosmiguelromoa@gmail.com")

        # Password
        self.label_password = Label(text="Password: ", font=("Courier", 8))
        self.label_password.grid(column=0, row=3, sticky="e")
        self.input_password = Entry(width=21)
        self.input_password.grid(column=1, row=3, sticky="w", columnspan=2)

        # Generate Password Button
        self.button_generate = Button(text="Generate Password", command=self.generate_password)
        self.button_generate.grid(column=2, row=3)

        # Save Button
        self.button_add = Button(text="Add", width=35, command=self.save_password)
        self.button_add.grid(column=1, row=5, columnspan=2)

    def generate_password(self):
        password = self.password_manager.generate_password()
        self.input_password.delete(0, END)
        self.input_password.insert(0, password)

    def save_password(self):
        website = self.input_website.get()
        email_username = self.input_email_username.get()
        password = self.input_password.get()

        if not website or not password:
            messagebox.showinfo(title="Error", message="Please fill out all fields.")
            return

        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email_username} | {password}\n")

        self.input_website.delete(0, END)
        self.input_password.delete(0, END)
        self.input_email_username.delete(0, END)
        messagebox.showinfo(title="Success", message="Data saved successfully!")