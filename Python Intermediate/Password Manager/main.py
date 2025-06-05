""" Password generator tool """
from random import choice, shuffle
from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry, Spinbox
from tkinter import messagebox
import json
import pyperclip

FILE_PATH = "./Password Manager/passwords.json"
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z']
upper_letters = [letter.upper() for letter in lower_letters]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
generator_widgets = []


# ---------------------------- PASSWORD GENERATOR --------------------- #
def generate_password():
    """ Generates a random password """
    # Generate password labels
    lower_label = Label(text="Number of lower case characters:")
    lower_label.grid(column=1, row=5, sticky="w")
    upper_label = Label(text="Number of upper case characters:")
    upper_label.grid(column=1, row=6, sticky="w")
    num_label = Label(text="Number of number characters:")
    num_label.grid(column=1, row=7, sticky="w")
    sym_label = Label(text="Number of symbol characters:")
    sym_label.grid(column=1, row=8, sticky="w")

    # Generate password spinboxes
    upper_sb = Spinbox(from_=0, to=10, width=16)
    upper_sb.grid(column=2, row=6, sticky="w")
    lower_sb = Spinbox(from_=0, to=10, width=16)
    lower_sb.grid(column=2, row=5, sticky="w")
    num_sb = Spinbox(from_=0, to=10, width=16)
    num_sb.grid(column=2, row=7, sticky="w")
    sym_sb = Spinbox(from_=0, to=10, width=16)
    sym_sb.grid(column=2, row=8, sticky="w")

    def generate():
        """ Generates user specified password """
        lower = int(lower_sb.get())
        upper = int(upper_sb.get())
        num = int(num_sb.get())
        sym = int(sym_sb.get())
        password_list = []
        l_letters = [choice(lower_letters) for char in range(lower)]
        u_letters = [choice(upper_letters) for char in range(upper)]
        nums = [choice(numbers) for char in range(num)]
        syms = [choice(symbols) for char in range(sym)]
        password_list = l_letters + u_letters + nums + syms
        shuffle(password_list)
        password_entry.insert(0, "".join(password_list))
        pyperclip.copy("".join(password_list))

    generate_button = Button(text="Generate", command=generate)
    generate_button.grid(column=2, row=9, sticky="w")

    # Store all widgets for future removal
    generator_widgets.extend([
        lower_label, lower_sb, upper_label, upper_sb,
        num_label, num_sb, sym_label, sym_sb, generate_button
    ])


# ---------------------------- SAVE PASSWORD -------------------------- #
def save():
    """ saves details to CSV, writes header only if file doesn't exist """
    website = web_entry.get().capitalize()
    username = user_entry.get()
    password = password_entry.get()
    new_data = {
        website:
        {
            "username": username,
            "password": password
            }
        }

    # Check if any fields left empty
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror("Oops", "You cannot leave a field blank")
    else:
        # Check if user wants to save
        is_ok = messagebox.askokcancel(
            website, f"Details entered:\n"
            f"Email/Username: {username}\nPassword: {password}"
            )
        if is_ok:
            # Open and update
            try:
                with open(FILE_PATH, "r", encoding="utf-8") as new_entry:
                    data = json.load(new_entry)

            # Save
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}

            data.update(new_data)
            with open(FILE_PATH, "w", encoding="utf-8") as new_entry:
                json.dump(data, new_entry, indent=4)

            # Reset entry screen
            web_entry.delete(0, "end")
            user_entry.delete(0, "end")
            password_entry.delete(0, "end")
            reset_generator_ui()
            web_entry.focus()


def reset_generator_ui():
    """ Destroy all password generator option widgets if they exist """
    for widget in generator_widgets:
        widget.destroy()
    generator_widgets.clear()


# ---------------------------- SEARCH --------------------------------- #
def web_search():
    """ search for web login """
    web = web_entry.get().capitalize()
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            messagebox.showinfo(web,
                                f"Username: {(data[web]["username"])}\n"
                                f"Password: {(data[web]["password"])}\n"
                                f"Your password has been copied"
                                )
            pyperclip.copy((data[web]["password"]))
    except (KeyError, FileNotFoundError):
        messagebox.showerror("Error", f"No data stored for {web}")


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1, sticky="w", padx=10)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky="w", padx=10)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="w", padx=10)

# Buttons
gen_password = Button(
    text="Generate Password", width=14, command=generate_password
    )
gen_password.grid(column=2, row=3)
add_password = Button(text="Add", width=43, command=save)
add_password.grid(column=1, row=10, columnspan=2, pady=5)
search_button = Button(text="Search", width=14, command=web_search)
search_button.grid(column=2, row=1)

# Entrys
web_entry = Entry(width=30)
web_entry.grid(column=1, row=1, sticky="w", pady=3)
web_entry.focus()
user_entry = Entry(width=51)
user_entry.grid(column=1, row=2, columnspan=2, sticky="w", pady=3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w", pady=3)

window.mainloop()
