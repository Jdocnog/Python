from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pwd_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pwd_numbers + pwd_letters + pwd_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as pwd_file:
                #reading old data
                data = json.load(pwd_file)
        except FileNotFoundError:
            with open("data.json", "w") as pwd_file:
                json.dump(new_data, pwd_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as pwd_file:
                #saving updated data
                json.dump(data, pwd_file, indent=4)
        finally:
            website_entry.delete('0', END)
            password_entry.delete('0', END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as pwd_file:
            # reading old data
            data = json.load(pwd_file)

            if website in data:
                messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\n"
                                                            f"Password: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exist")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid_rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1)
website_entry.focus()

#username label and entry
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=45)
username_entry.grid(column=1, row=2)
username_entry.insert(0, "jordan@email.com")

#password label and entry
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry(width=45)
password_entry.grid(column=1, row=3)

#generate password button
gen_password_button = Button(text="Generate Password", command=generate_password, width=15)
gen_password_button.grid(column=2, row=3)

#add info to txt button
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4)

#Search button
search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1)









window.mainloop()