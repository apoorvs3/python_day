from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.minsize(width=350, height=500)
        self.window.config(pady=20, padx=20)
        self.label_score  = Label(text='Score: ')
        self.label_score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='green')
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.button = Button()
        self.window.mainloop()

