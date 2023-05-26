from tkinter import *
from tkinter import messagebox
import json
import pyperclip
import password_generator as pg

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search_account():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        f_website = website_entry.get().lower()
        if f_website in data:
            email = data[f_website]["email"]
            password = data[f_website]["password"]
            messagebox.showinfo(title=f_website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {f_website} exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, pg.password)
    pyperclip.copy(pg.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_account():
    f_website = website_entry.get().lower()
    f_email = email_entry.get().lower()
    f_password = password_entry.get()
    new_data = {
        f_website: {
            "email": f_email,
            "password": f_password,
        }
    }

    if f_website == "" or f_email == "" or f_password == "":
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file) #reading old data

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)  # saving updated data

        else:
            data.update(new_data) #updating old data with new data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # saving updated data

        finally:
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
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()
default_email = StringVar(value="mkko@seznam.cz")
email_entry = Entry(width=51, textvariable=default_email)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

#Buttons
generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")
add_button = Button(text="Add", width=43, command=save_account)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")
search_button = Button(text="Search", width=14, command=search_account)
search_button.grid(column=2, row=1, sticky="w")


window.mainloop()
