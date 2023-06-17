import turtle

name = turtle.Turtle()

name.reset()
name.pencolor('white')
name.pensize(5)
name.penup()
name.goto(-300,200)
name.speed(3)


#Z
name.pendown()
name.fd(100)
name.goto(-300,100)
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
name.goto(-50, 100)

#K
name.pendown()
name.rt(90)
name.fd(100)
name.bk(50)
name.goto(0, 200)
name.goto(-50, 150)
name.goto(0, 100)

name.penup()
name.rt(90)
name.fd(30)

#I
name.pendown()
name.lt(90)
name.fd(100)
name.bk(100)



turtle.bgcolor('black')
turtle.done()
