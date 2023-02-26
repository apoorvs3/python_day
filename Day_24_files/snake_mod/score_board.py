from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        with open('data.txt', mode='r') as file:
            content = file.read()
        self.high_score = int(content)
        super().__init__()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score}, High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
        with open('data.txt', mode='w') as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'Game Over', align=ALIGNMENT, font=FONT)
