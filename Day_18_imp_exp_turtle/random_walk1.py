import random
from turtle import Turtle, Screen

amun = Turtle()
screen = Screen()
screen.colormode(255)
# colors = ['red', 'green', 'yellow', 'orange', 'blue', 'green', 'cyan', 'violet']
angles = [90, 180, 270, 360]
direction = ['left', 'right']


def turns(angle):
    # can use amun.setheading
    dir_ = random.choice(['right', 'left'])
    if dir_ == 'right':
        amun.right(angle)
    elif dir_ == 'left':
        amun.left(angle)


def moves():
    amun.speed(0)
    random_path = random.randint(10, 25)
    return amun.forward(random_path)


def looks():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    amun.pensize(5)
    return amun.color(r, g, b)


for _ in range(100):
    random_angle = random.choice(angles)
    looks()
    moves()
    turns(random_angle)


screen.exitonclick()
