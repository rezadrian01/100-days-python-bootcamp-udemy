import pyperclip
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

BASE_PATH = "section 29"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    is_empty = len(website.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0
    if is_empty:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(f"{website}", message=f"These are details entered\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
    if is_ok:
        with open(f"{BASE_PATH}/data.txt", mode='a') as data:
            data.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=f"{BASE_PATH}/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


#inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky='EW')
website_input.focus()
email_input = Entry(width=35)
email_input.insert(0, 'ahmad@gmail.com')
email_input.grid(column=1, row=2, columnspan=2, sticky='EW')
password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=1, sticky='EW')

#buttons
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3, sticky='EW')
add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')




window.mainloop()