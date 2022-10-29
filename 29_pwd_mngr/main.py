from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [random.choice(letters) for item_l in range(nr_letters)]
    symbols_list = [random.choice(symbols) for item_s in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for item_n in range(nr_numbers)]

    password_list += letters_list + symbols_list + numbers_list
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)  # already copied


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_inputs():
    website_input.delete(first=0, last=len(website_input.get()))
    password_input.delete(first=0, last=END)


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='warning', message='Please don\'t leave any field empty')
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(),
                                       message=f'These are details entered\nwebsite: {website}\npassword: {password}\nProceed?')
        if is_ok:
            with open(file='data.txt', mode='a') as file:
                file.write(f'{website} | {email} | {password}')
                file.write('\n')
                clear_inputs()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(height=220, width=220)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text='Email/Username: ')
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'apoorv@hap.com')

password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)
password_input = Entry(width=18)
password_input.grid(column=1, row=3)
generate_password_button = Button(text='Generate Password', command=generate_passwords)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
