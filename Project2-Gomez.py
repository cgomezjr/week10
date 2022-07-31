from turtle import Turtle
import random
t = Turtle()
def cCurve(t, x1, y1, x2, y2, level):
    """Draws a c-curve of the given level."""
    def drawLine(x1, y1, x2, y2):
        """Draws a line segment between the endpoints."""
        
        color = random.randint(1,8)
        if color == 1:
            color = "black"
        elif color == 2:
            color = "white"
        elif color == 3:
            color ="blue"
        elif color == 4:
            color ="green"
        elif color == 5:
            color = "red"
        elif color == 6:
            color ="cyan"
        elif color == 7:
            color ="magenta"
        elif color == 8:
            color ="yellow"
        t.pencolor(color)

##        r = random.randint(0, 255)
##        g = random.randint(0, 255)
##        b = random.randint(0, 255)
##        t.pencolor(r, g, b)
        
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
    if level == 0:
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)

cCurve(t, 0, -150, 0, 150, 14)

