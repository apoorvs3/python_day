import random
from turtle import Turtle, Screen

amun = Turtle()


colors = ['red', 'green', 'yellow', 'orange', 'blue', 'green', 'cyan', 'violet']
angles = [90, 180, 270, 360]


while True:
    random_path = random.randint(10, 25)
    random_angle = random.choice(angles)
    random_direction = ['right', 'left']
    random_color = random.choice(colors)

    amun.color(random_color)
    amun.pensize(5)
    amun.forward(random_path)
    amun.speed(0)
    direction = random.choice(random_direction)
    if direction == 'right':
        amun.right(random_angle)
    else:
        amun.left(random_angle)

screen = Screen()
screen.exitonclick()
