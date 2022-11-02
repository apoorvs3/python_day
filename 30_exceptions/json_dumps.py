from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random


# ----------------------------- Find Password ------------------------------------ #

def search():
    website = website_input.get()
    # try to use more if else
    try:
        with open(file='data.json', mode='r') as file:
            content = json.load(file)
            try:
                messagebox.showinfo(title='Results',
                                    message=f"email: {content[website]['email']}\nPassword: {content[website]['password']}")
            except KeyError:
                messagebox.showwarning(title='Error 404', message='No such website saved')
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title='File corrupt', message='No data in the our Database')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


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
    my_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='warning', message='Please don\'t leave any field empty')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(my_data)
        except JSONDecodeError or FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(my_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            clear_inputs()


"""
code for JSON
             # write data to json file
                # json.dump(my_data, file, indent=4)

                # read data
                # var = json.load(file)
                # print(var)

                # update data - load then update, then dump
                data_ = json.load(data_file)
                print(data_)
                # data.update(my_data)

            with open(file='data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)
                clear_inputs()

"""

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text='search', width=8, command=search)
search_button.grid(column=2, row=1)

email_label = Label(text='Email/Username: ')
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'apoorv@hap.com')

password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)
password_input = Entry(width=18)
password_input.grid(column=1, row=3)
generate_password_button = Button(text='Generate Password', width=13, command=generate_passwords)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
