import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
ra = Turtle()
ra.pensize(1)
ra.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(2):
    ra.color(random_color())
    ra.circle(100)

ra.hideturtle()
screen.exitonclick()
