from turtle import Turtle
import math
t = Turtle()
def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(0, 120):
        t.forward(2 * math.pi * radius / 120)
        t.left(3)

drawCircle(t, 0, -200, 100)
drawCircle(t, 0, 0, 75)
drawCircle(t, 0, 150, 50)
