from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.write('Level 1', move=False, align='center', font=FONT)
        self.penup()
        self.goto(-280, 280)
