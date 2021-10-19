from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V',
               'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

    # list comprehension where _ is used because it does not matter what it is
    password_letters = [choice(letters) for _ in range(6, 10)]
    password_symbols = [choice(symbols) for _ in range(2, 4)]
    password_numbers = [choice(numbers) for _ in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    website_password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    with open("data.txt", "a") as file:
        website = website_label_input.get()
        user_email = website_user_input.get()
        password = website_password_input.get()

        if len(website) == 0 or len(password) == 0:
            is_empty = messagebox.showinfo(title="Warning", message="You can not have empty fields!")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"Details entered are:\n Email: {user_email}\n "
                                                                  f"Password: {password}\n Is this ok to save?")

            if is_ok:
                file.write(f"{website} | {user_email} | {password}\n")
                website_label_input.delete(0, END)
                website_password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Input fields
website_label_input = Entry(width=60)
website_label_input.grid(column=1, row=1, columnspan=2)
website_label_input.focus()
website_user_input = Entry(width=60)
website_user_input.grid(column=1, row=2, columnspan=2)
website_user_input.insert(0, "your-email@email.com")
website_password_input = Entry(width=41)
website_password_input.grid(column=1, row=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_user = Label(text="Email/Username:")
website_user.grid(column=0, row=2)
website_password = Label(text="Password:")
website_password.grid(column=0, row=3)

# Button
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)
add_button = Button(text="Add", width=51, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
