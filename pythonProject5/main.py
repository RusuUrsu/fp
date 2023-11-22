import time
import turtle

def draw_heart():
    pen = turtle.Pen()
    pen.left(90)

    pen2 = turtle.Pen()
    pen2.left(90)

    cx = pen.xcor()

    for i in range(0,181,2):
        pen.forward(1)
        pen.right(2)

        pen2.forward(1)
        pen2.left(2)

    for i in range(0,45,2):
        pen.forward(1)
        pen.right(2)


        pen2.forward(1)
        pen2.left(2)




    while int(pen.xcor()) != int(cx):
        pen.forward(1)
        pen2.forward(1)

    turtle.done()




def draw_rectangle():
    pen = turtle.Pen()
    pen2 = turtle.Pen()

    pen2.penup()
    pen2.goto(37.5,-75)
    pen2.pendown()


    pen.forward(100)
    pen2.forward(25)

    pen.right(90)
    pen2.right(90)

    pen.forward(200)
    pen2.forward(50)

    pen.right(90)
    pen2.right(90)

    pen.forward(100)
    pen2.forward(25)

    pen.right(90)
    pen2.right(90)

    pen.forward(200)
    pen2.forward(50)

    turtle.done()


def draw_houses():
    pen = turtle.Pen()
    pen2 = turtle.Pen()

    pen2.penup()
    pen2.goto(-310,0)
    pen2.pendown()

    #body
    for i in range(4):
        pen.forward(300)
        pen2.forward(300)

        pen.right(90)
        pen2.right(90)

    #roof
    pen.left(45)
    pen2.left(45)

    while int(pen.xcor()) < 150:
        pen.forward(5)
        pen2.forward(5)

    pen.right(90)
    pen2.right(90)

    while int(pen.ycor()) > 0:
        pen.forward(5)
        pen2.forward(5)


    #door
    pen.penup()
    pen2.penup()

    pen.goto(140,-300)
    pen2.goto(-165,-300)

    pen.pendown()
    pen2.pendown()

    pen.left(135)
    pen2.left(135)
    pen.forward(70)
    pen2.forward(70)
    pen.right(90)
    pen2.right(90)
    pen.forward(40)
    pen2.forward(40)
    pen.right(90)
    pen2.right(90)
    pen.forward(70)
    pen2.forward(70)

    #window
    pen.penup()
    pen2.penup()
    pen.goto(140,-150)
    pen2.goto(-165,-150)
    pen.pendown()
    pen2.pendown()

    pen.right(180)
    pen2.right(180)

    for i in range(4):
        pen.forward(40)
        pen2.forward(40)
        pen.right(90)
        pen2.right(90)

    turtle.done()



def main():



    while True:
        x = int(input("""
            1 -> Rectangle
            2 -> Heart
            3 -> Houses
            0 -> exit

            """))
        if x == 1:
            draw_rectangle()
        if x == 2:
            draw_heart()
        if x == 3:
            draw_houses()
        if x == 0:
            break





main()



