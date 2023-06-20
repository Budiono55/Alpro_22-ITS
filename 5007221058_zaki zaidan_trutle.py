#Zaki Zaidan Akbar 
#5007221058

#show name and repeat it 6 times using different color 


import turtle

name = turtle.Turtle()

name.reset()
#name.pencolor('white')
turtle.bgcolor('black')

color = ['yellow','cyan','white','green','red','grey','purple']
x=0
xs=0
yp=0
xc=0

#how many times this word will be printed
xtimes=6


while x<=xtimes:
    name.pensize(5)
    name.penup()
    name.goto(-400,400+yp)
    name.speed(4+xs)
    name.pencolor(color[xc])
    


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

    name.penup()
    name.fd(100)
    name.lt(60)

    ##
    name.pendown()
    name.fd(120)
    name.rt(60)

    name.penup()
    name.fd(50)
    name.rt(120)
    name.pendown()
    name.fd(120)
    name.rt(60)

    name.penup()
    name.fd(-75)
    name.rt(90)
    name.fd(80)
    name.lt(90)

    name.pendown()
    name.fd(120)
    name.penup()

    name.lt(90)
    name.fd(40)
    name.lt(90)

    name.pendown()
    name.fd(110)
    #maybe art?
    #name.rt(30)

    #lines

    x+=1
    xc+=1
    xs+=2
    yp-=120

turtle.done()
