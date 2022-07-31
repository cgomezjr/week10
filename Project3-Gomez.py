from turtle import *
  
def drawFractalLine(lengthSide, level):
    
    if level == 0:
        forward(lengthSide)
    else:
        lengthSide /= 3.0
        drawFractalLine(lengthSide, level - 1) 
        left(60) 
        drawFractalLine(lengthSide, level - 1) 
        right(120) 
        drawFractalLine(lengthSide, level - 1) 
        left(60) 
        drawFractalLine(lengthSide, level - 1) 

def snowflake(distance, level):
    for i in range(3):     
        drawFractalLine(distance, level) 
        right(120)
        
snowflake(200, 2)

