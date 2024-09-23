import turtle

screen = turtle.Screen()
screen.bgcolor('white')
turtle.speed(10)
turtle.colormode(255)
turtle.pencolor(255,255,255)

scaleoftable = int(input("Enter a size for the table from 1 to 100"))

while scaleoftable > 100 or scaleoftable < 1:
    scaleoftable = int(input("Enter a size for the table from 1 to 100 again please"))

def tabletop():
    turtle.penup()
    turtle.goto(-3 * scaleoftable, 1 * scaleoftable)
    turtle.pendown()
    turtle.fillcolor(76,50,40)
    turtle.begin_fill()
    turtle.forward(6 * scaleoftable)
    turtle.right(90)
    turtle.forward(0.4 * scaleoftable)
    turtle.right(90)
    turtle.forward(6 * scaleoftable)
    turtle.right(90)
    turtle.forward(0.2 * scaleoftable)
    turtle.right(90)
    turtle.end_fill()

def frontleg_table(x, y):
    turtle.pencolor(76,50,40)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(76,50,40)
    turtle.begin_fill()
    turtle.forward(0.25 * scaleoftable)
    turtle.right(90)
    turtle.forward(3 * scaleoftable)
    turtle.right(90)
    turtle.forward(0.25 * scaleoftable)
    turtle.right(90)
    turtle.forward(3 * scaleoftable)
    turtle.right(90)
    turtle.end_fill()

def Backleg_table(x, y):
    turtle.pencolor(76,50,40)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(76,50,40)
    turtle.begin_fill()
    turtle.forward(0.25 * scaleoftable)
    turtle.right(90)
    turtle.forward(2.3 * scaleoftable)
    turtle.right(90)
    turtle.forward(0.25 * scaleoftable)
    turtle.right(90)
    turtle.forward(2.3 * scaleoftable)
    turtle.right(90)
    turtle.end_fill()

tabletop()
frontleg_table(-3 * scaleoftable, 0.7 * scaleoftable) #front left leg # finished
Backleg_table(2 * scaleoftable, 0.7 * scaleoftable) #back right leg
Backleg_table(-2 * scaleoftable, 0.7 * scaleoftable) #back left leg
frontleg_table(2.75 * scaleoftable, 0.7 * scaleoftable) #front right leg #finished

screen.mainloop()