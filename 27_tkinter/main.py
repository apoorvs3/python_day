import tkinter

"""
https://docs.python.org/3/library/tkinter.html#the-packer
"""

window = tkinter.Tk()
window.title('A GUI Program')
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24))
my_label.pack()

window.mainloop()
