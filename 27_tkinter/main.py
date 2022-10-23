import time
from tkinter import *

"""
https://docs.python.org/3/library/tkinter.html#the-packer
https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
"""


def button_clicked():
    print('I got clicked')
    my_label.config(text='Button is clicked')
    time.sleep(2)
    my_label.config(text=input.get())


window = Tk()
window.title('A GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = Label(text='I am a label', font=('Arial', 24))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# button
button = Button(text='Click me', command=button_clicked)  # notice function is not getting called
# button.pack()
button.grid(column=1, row=1)

button1 = Button(text='New button')
button1.grid(column=2, row=0)
# entry component
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
