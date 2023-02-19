import time
from turtle import Turtle, Screen

ka = Turtle()
ka.speed(2)
screen = Screen()
# screen.listen()
# screen.onkey(ka.setheading(90), 'w')
# screen.onkey(ka.setheading(180), 's')


ka.forward(20)
time.sleep(2)

ka.setheading(90)
ka.forward(20)
time.sleep(2)

ka.setheading(180)
ka.forward(20)
time.sleep(2)

ka.setheading(270)
ka.forward(20)
time.sleep(2)





screen.exitonclick()
