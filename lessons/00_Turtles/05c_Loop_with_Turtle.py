
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import turtle
turtle.setup (width=600, height=600)
tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape('turtle')
tina.speed(1)

tina.circle(100)
tina.penup()
tina.goto(-50 , 100)
tina.pendown()
tina.circle(25)
tina.penup()
tina.goto(0 , 0)
tina.pendown()
tina.circle(30)
tina.left(90)
tina.penup()
tina.forward(200)
tina.left(90)
tina.pendown()
tina.forward(70)
tina.right(90)
tina.forward(16)
tina.right(90)
tina.forward(19)
tina.left(90)
tina.forward(60)
tina.right(90)
tina.forward(65)
tina.right(90)
tina.forward(50)
tina.right()














































turtle.exitonclick()