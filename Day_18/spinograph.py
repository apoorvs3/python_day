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


def draw_spinograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        ra.color(random_color())
        ra.circle(100)
        ra.setheading(ra.heading() + size_of_gap)


draw_spinograph(5)
ra.hideturtle()
screen.exitonclick()
