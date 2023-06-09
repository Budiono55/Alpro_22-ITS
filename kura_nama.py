import turtle

name = turtle.Turtle()

name.reset()
name.pencolor('black')
name.pensize(5)
name.penup()
name.goto(-300,200)
name.speed(1)

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


name.mainloop()