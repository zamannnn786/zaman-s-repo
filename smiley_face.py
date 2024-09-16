import turtle

def draw_centered_circle(x, y, radius, fill_color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.forward(radius)
    turtle.left(90)
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.setheading(25)



def draw_smiley(x, y, head_radius, head_color, nose_color):

    draw_centered_circle(x, y, head_radius, head_color)

    draw_centered_circle(x, y, head_radius, head_color // 10, nose_color)

def draw_eye(x, y, eye_radius, iris_color):

    draw_centered_circle(x, y, eye_radius, 'white')

    iris_radius = eye_radius * 0.5
    draw_centered_circle(x, y, iris_radius, iris_color)

    pupil_radius = eye_radius * 0.25
    draw_centered_circle(x, y, pupil_radius, 'black')

def tweak(speed, tracer_on):
    turtle.speed(speed)
    turtle.tracer(tracer_on)
    
def main():
    turtle.hideturtle()
    tweak(1, True)
    draw_smiley(0,0,100,'red','orange')
    eye_distance_x = 0.35 * 100
    eye_distance_y = 0.25 * 100
    eye_radius = 0.25 * 100
    draw_eye(eye_distance_x, eye_distance_y, eye_radius, 'blue')
    draw_eye(eye_distance_x, eye_distance_y, eye_radius, 'blue')    

main()