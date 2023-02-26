import random
from turtle import Turtle, Screen
colors = ['red', 'green', 'yellow', 'orange', 'blue', 'green']
ka = Turtle()
ka.speed(1)
for sides in range(3, 11):  # from triangle to decagon
    ka.color(random.choice(colors))
    for _ in range(sides):
        ka.forward(100)
        ka.right(360 / sides)

screen = Screen()
screen.exitonclick()
