import turtle

name = turtle.Turtle()

name.reset()
name.pencolor('white')
turtle.bgcolor('black')

x=0
xs=0
yp=0

while x<=3:
    name.pensize(5)
    name.penup()
    name.goto(-300,200+yp)
    name.speed(2+xs)


    #Z
    name.pendown()
    name.fd(100)
    name.rt(135)
    name.fd(140)
    name.lt(135)
    name.fd(100)

    name.penup()
    name.fd(50)

    #A
    name.pendown()
    name.lt(90)
    name.fd(100)
    name.rt(90)
    name.fd(50)
    name.rt(90)
    name.fd(100)
    name.bk(40)
    name.rt(90)
    name.fd(50)

    name.penup()
    name.rt(180)
    name.fd(100)
    name.rt(90)
    name.fd(41)
    name.rt(180)

    #K
    name.pendown()
    name.fd(100)
    name.bk(50)
    name.rt(45)
    name.fd(70)
    name.bk(70)
    name.rt(90)
    name.fd(70)

    name.lt(45)
    name.penup()
    name.fd(30)

    #I
    name.pendown()
    name.lt(90)
    name.fd(100)
    name.bk(100)
    name.rt(90)

    x+=1
    xs+=2
    yp-=120

turtle.done()
