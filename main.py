from tkinter import *
import random

FONT = ("Arial", 12, "bold")
FILE_NAME = "data.txt"

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
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open(file="data.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sudesh@gmail.com")

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_password_button = Button(
    text="Generate Password", width=20, command=generate_password
)
generate_password_button.grid(row=4, column=1, columnspan=2)

add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=5, column=0, columnspan=3)

window.mainloop()
