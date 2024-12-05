import turtle as tur
from numpy import *

tur.speed(10)

def draw(start_x, start_y, color):
    # Set initial position
    tur.penup ()
    tur.goto(start_x, start_y)
    tur.pendown ()

    # flower base
    tur.fillcolor (color)
    tur.begin_fill ()
    tur.circle (10,180)
    tur.circle (25,110)
    tur.left (50)
    tur.circle (60,45)
    tur.circle (20,170)
    tur.right (24)
    tur.fd (30)
    tur.left (10)
    tur.circle (30,110)
    tur.fd (20)
    tur.left (40)
    tur.circle (90,70)
    tur.circle (30,150)
    tur.right (30)
    tur.fd (15)
    tur.circle (80,90)
    tur.left (15)
    tur.fd (45)
    tur.right (165)
    tur.fd (20)
    tur.left (155)
    tur.circle (150,80)
    tur.left (50)
    tur.circle (150,90)
    tur.end_fill ()

    # Petal 1
    tur.left (150)
    tur.circle (-90,70)
    tur.left (20)
    tur.circle (75,105)
    tur.setheading (60)
    tur.circle (80,98)
    tur.circle (-90,40)

    # Petal 2
    tur.left (180)
    tur.circle (90,40)
    tur.circle (-80,98)
    tur.setheading (-83)

    # Leaves 1
    tur.fd (30)
    tur.left (90)
    tur.fd (25)
    tur.left (45)
    tur.fillcolor ("green")
    tur.begin_fill ()
    tur.circle (-80,90)
    tur.right (90)
    tur.circle (-80,90)
    tur.end_fill ()
    tur.right (135)
    tur.fd (60)
    tur.left (180)
    tur.fd (85)
    tur.left (90)
    tur.fd (80)

    # Leaves 2
    tur.right (90)
    tur.right (45)
    tur.fillcolor ("green")
    tur.begin_fill ()
    tur.circle (80,90)
    tur.left (90)
    tur.circle (80,90)
    tur.end_fill ()
    tur.left (135)
    tur.fd (60)
    tur.left (180)
    tur.fd (60)
    tur.right (90)
    tur.circle (200,60)

def heart(start_x, start_y, color, scale):
    tur.up()
    tur.goto(start_x, start_y)
    tur.down()

    # color
    tur.fillcolor(color)
    tur.begin_fill()

    # \
    x = 500 * scale
    t = 140
    tur.right(t)
    tur.forward(x)

    # /-\ (x2)
    tur.right(180 - t)
    tur.circle(-x * sin(deg2rad(180 - t))/2, 180) # radius, angle
    tur.left(180)
    tur.circle(-x * sin(deg2rad(180 - t))/2, 180) # radius, angle

    # /
    tur.right(180 - t)
    tur.forward(x)
    tur.end_fill()

    # text - position
    tur.up()
    tur.left(180 - t)
    tur.forward(100)
    tur.right(90)
    tur.forward(200 * scale)

def main():
    tur.bgcolor("pink")
    draw(0, 300, 'red')
    draw(-100, 225, 'orange')
    tur.left(45)
    draw(100, 250, 'yellow')
    draw(15, 150, 'white')
    tur.write("Happy Valentine's Day,\nmy juicy soup dumpling! <3", align= "left", font=("Script", 30, "bold"))

    tur.setheading(-75)
    heart(-250, 250, 'magenta', 0.1)
    tur.setheading(-105)
    heart(250, 250, 'light green', 0.1)
    tur.Screen().exitonclick()

if __name__ == "__main__": main()

