from turtle import Turtle

LEFT_ORDINATES = (-350, 0)
RIGHT_ORDINATES = (350, 0)


class Paddle(Turtle):
    def __int__(self, position):
        super().__init__('square')
        self.color('White')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if position == 'RIGHT':
            self.goto(RIGHT_ORDINATES)
        else:
            self.goto(LEFT_ORDINATES)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
