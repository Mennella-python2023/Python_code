
import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)

# Draw the square (house body)
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.begin_fill()
pen.color("lightblue")
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# Draw the roof
pen.begin_fill()
pen.color("brown")
pen.goto(-100, 100)
pen.goto(0, 200)
pen.goto(100, 100)
pen.goto(-100, 100)
pen.end_fill()

# Draw the door
pen.penup()
pen.goto(-30, -100)
pen.pendown()
pen.begin_fill()
pen.color("darkred")
for _ in range(2):
    pen.forward(60)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# Draw windows
pen.penup()
pen.goto(-80, 20)
pen.pendown()
pen.begin_fill()
pen.color("yellow")
for _ in range(4):
    pen.forward(40)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(40, 20)
pen.pendown()
pen.begin_fill()
for _ in range(4):
    pen.forward(40)
    pen.left(90)
pen.end_fill()

# Hide the turtle and display the drawing
pen.hideturtle()
turtle.done()
