#CTI - 110
#P4LAB2: Initials
#Bradley Legge
#3/25/2018

import turtle
wn = turtle.Screen()

initial = turtle.Turtle()
initial.color("red")
initial.pensize(5)

initial.left(90)
initial.forward(210)
initial.right(90)
initial.forward(30)
for i in range(15):
    initial.right(10)
    initial.forward(10)
initial.right(30)
initial.forward(50)
initial.right(180)
initial.forward(30)
for i in range(15):
    initial.right(10)
    initial.forward(10)
initial.right(30)
initial.forward(50)
initial.right(180)

initial.penup()
initial.forward(100)
initial.pendown()

initial.left(90)
initial.forward(210)
initial.right(160)
initial.forward(120)
initial.left(140)
initial.forward(120)
initial.right(160)
initial.forward(210)
initial.left(90)

initial.penup()
initial.forward(20)
initial.pendown()

initial.left(90)
initial.forward(210)
initial.left(180)
initial.forward(210)
initial.left(90)
initial.forward(80)




wn.mainloop()

