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


def print_hello_world():
   message = "hello, world"
   print(message)

print_hello_world()



def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} არის ლუწი")
    else:
        print(f"{number} არის კენტი")

even_or_odd(23)
even_or_odd(42)


def cube():
    for i in range(120):
        print("******")

cube()


def print_pattern():
    rows = 4
    for i in range(rows):
        spaces = " " * i
        stars = "*" * (7 if i < 2 else 8)
        print(spaces + stars)

print_pattern()




    