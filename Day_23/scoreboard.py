from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.write(f'Level {self.score}', move=False, align='center', font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f'Level {self.score}', move=False, align='center', font=FONT)

    def game_over(self):
        game = Turtle()
        game.write(f'Game Over !!! ', move=False, align='center', font=FONT)