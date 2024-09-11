import turtle

def square(px, ang, color):
    turtle.speed(1)
    turtle.pensize(10)
    turtle.bgcolor('pink')
    turtle.fillcolor(color)
    turtle.pencolor('white')
    # to fill the color in the square
    turtle.begin_fill()
    turtle.forward(px)
    turtle.left(ang)
    turtle.forward(px)
    turtle.left(ang)
    turtle.forward(px)
    turtle.left(ang)
    turtle.forward(px)
    turtle.left(ang)
    turtle.end_fill()



def main():
    fillcolor = input("Okease select a color to full the squares")

    pixels = 150
    angle = 90
    square(pixels, angle, fillcolor)

    fillcolor = input("Okease select a color to full the squares")

    pixels = 100
    angle = 90
    square(pixels, angle, fillcolor)

    fillcolor = input("Okease select a color to full the squares")

    pixels = 70
    angle = 90
    square(pixels, angle, fillcolor)

    
    
    pixels = int(input("Please enter how many pixels do you want the turtle to move"))
    angle = int(input("Please enter how much of an angel you want the turtle to move at"))
    color = input("Please enter the color you want to add")

    square(pixels, angle, color)
    input("please enter any key")


main()