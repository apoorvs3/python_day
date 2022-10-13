from turtle import Turtle, Screen

jim = Turtle()
jim.color('blue')

for _ in range(15):
    jim.forward(10)
    jim.penup()
    jim.forward(10)
    jim.pendown()


screen = Screen()
screen.exitonclick()
