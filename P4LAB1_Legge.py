#CTI-110
#P4LAB1: Shapes
#Bradley Legge
#3/25/2018

import turtle
wn = turtle.Screen()
square = turtle.Turtle()
triangle = turtle.Turtle()

triangle.color("red")

for i in range(4):
    square.forward(50)
    square.left(90)

for i in range(3):
    triangle.forward(90)
    triangle.left(120)

