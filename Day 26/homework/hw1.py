from turtle import *

def triangle(color, x, y):
   penup()
   goto(x, y)
   pendown()
   fillcolor(color)
   begin_fill()
   for i in range(3):
      forward(50)
      left(120)
      end_fill()

width(10)
speed(5)
color("green")
triangle("green", 0, 0)
color("blue")
triangle("blue", 100, 100)
color("red")
triangle("red", -100, -100)

exitonclick()