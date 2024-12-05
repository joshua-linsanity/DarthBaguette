from turtle import *
from numpy import *

def main():
    # init
    up()
    right(90)
    forward(200)
    down()

    # color
    fillcolor('red')
    begin_fill()

    # \
    x = 500
    t = 140
    right(t)
    forward(x)

    # /-\ (x2)
    right(180 - t)
    circle(-x * sin(deg2rad(180 - t))/2, 180) # radius, angle
    left(180)
    circle(-x * sin(deg2rad(180 - t))/2, 180) # radius, angle

    # /
    right(180 - t)
    forward(x)
    end_fill()

    # text - position
    up()
    left(180 - t)
    forward(100)
    right(90)
    forward(200)

    # text - write
    down()
    color('red')
    write('BinBin <3 Kimchi!', 
          font=("Lucida Calligraphy", 30, "normal"),
          move=True)

    # done
    done()

if __name__ == '__main__': 
    main()

