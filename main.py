from tkinter import *
from tkinter import messagebox
import random
import json

FONT = ("Arial", 12, "bold")
FILE_NAME = "data.json"

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SYMBOLS = [")", "!", "@", "#", "$", "%", "^", "&", "*", "("]

LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_random_password():
    nr_letters = random.randint(7, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(4, 6)

    letters_list = [random.choice(LETTERS) for _ in range(nr_letters)]
    symbols_list = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    numbers_list = [random.choice(NUMBERS) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    return password


def generate_password():
    password = generate_random_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def confirmation_to_save(user_data, website):
    save_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered :\nEmail : {user_data["email"]}\nPassword : {user_data["password"]}\n\nIs it okay to save?",
    )

    if save_ok:
        return True

    return False


def read_file():
    try:
        file = open(FILE_NAME, mode="r")
        return json.load(file)
    except:
        file = open(FILE_NAME, mode="w")
        json.dump({}, file, indent=4)
        return {}
    finally:
        file.close()


def update_file(new_data, data):
    with open(FILE_NAME, mode="w") as file:
        data.update(new_data)
        json.dump(data, file, indent=4)


def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror(
            title="Error!",
            message="Please make sure you haven't left any fields empty.",
        )
        return

    new_data = {website: {"email": email, "password": password}}

    if not confirmation_to_save(website=website, user_data=new_data[website]):
        return

    data = read_file()
    update_file(data=data, new_data=new_data)
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- SEARCH UP ------------------------------- #
def search():
    data = read_file()
    website = website_entry.get().lower()

    try:
        if not website:
            raise NameError

        user_data = data[website]

    except NameError:
        messagebox.showerror(
            title="Search Error", message="Please enter the website name"
        )
    except KeyError:
        messagebox.showerror(title="Search Error", message="Data not found")
    else:
        messagebox.showinfo(
            title=website,
            message=f"Email : {user_data["email"]}\nPassword : {user_data["password"]}",
        )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website :")
website_label.grid(row=1, column=0)
email_label = Label(text="Email :")
email_label.grid(row=2, column=0)
password_label = Label(text="Password :")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=30)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "sudesh@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", command=search, width=13)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate", command=generate_password, width=13)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
