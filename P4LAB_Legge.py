#CTI-110
#P4LAB: Nested Loops
#Bradley Legge
#3/25/2018

import turtle
snowflake = turtle.Turtle()
snowflake.pensize(3)
snowflake.pencolor("cornflower blue")


def branch():
  for i in range(3):
      for i in range(3):
          snowflake.backward(30)
          snowflake.forward(30)
          snowflake.right(45)
      snowflake.left(90)
      snowflake.backward(30)
      snowflake.left(45)
  snowflake.right(90)
  snowflake.forward(90)

for i in range(8):
    branch()
    snowflake.left(45)

    

  
