from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def on_click():
    kms = round(float(inp.get()) * 1.609344, 2)
    label_answer.config(text=kms)


# input miles
label_mile = Label(text='Miles')
label_mile.grid(row=0, column=2)
label_kilo = Label(text='Km')
label_kilo.grid(row=1, column=2)
label_equals = Label(text='is equal to: ')
label_equals.grid(row=1, column=0)
label_answer = Label(text='        ')
label_answer.grid(row=1, column=1)

# button
button = Button(text='Calculate', command=on_click)
button.grid(row=2, column=1)

# entry points
inp = Entry(width=15)
inp.grid(row=0, column=1)
window.mainloop()
