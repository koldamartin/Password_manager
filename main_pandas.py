#STEJNA VERZE JAKO main.py akorat zapisuje do pandas,
#chybi zde  Handling exceptions
#Chybi zde search button

from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import pyperclip
import password_generator as pg

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#nefunguje to
def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, pg.password)
    pyperclip.copy(pg.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_account():
    f_website = website_entry.get()
    f_email = email_entry.get()
    f_password = password_entry.get()

    if f_website == "" or f_email == "" or f_password == "":
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title="Entry succesful", message=f"These are the details entered:\n"
                                                         f"Website: {f_website}\n"
                                                         f"Email/Username: {f_email}\n"
                                                         f"Password: {f_password}\n"
                                                         f"Do you want to save it?")
        if is_ok:
            if not os.path.isfile("data.csv"):
                df = pd.DataFrame(columns=["website", "email", "password"])
            else:
                df = pd.read_csv("data.csv")
            new_row = {"website": f_website, "email": f_email, "password": f_password}
            df = pd.concat([df, pd.DataFrame(new_row, index=[0])], ignore_index=True)
            df.to_csv("data.csv", index=False)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("arial", 10))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("arial", 10))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("arial", 10))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()
default_email = StringVar(value="mkko@seznam.cz")
email_entry = Entry(width=51, textvariable=default_email)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
password_entry = Entry(width=29)
password_entry.grid(column=1, row=3, sticky="w")

#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")
add_button = Button(text="Add", width=43, command=save_account)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
