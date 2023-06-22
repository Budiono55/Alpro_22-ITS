# Zaki Zaidan Akbar
# 5007221058


import turtle

# simplyfy the turtle function with the variable "pen"
pen = turtle.Turtle()

# build a list of the color intended to use later
color = ['blue', 'orange', 'black', 'green', 'red']
pen.speed(2)
pen.pensize(7)
# circle diameter can be changed without destroying the picture
CIRCLE_DIAMETER = 75 

# start writing the first circle
pen.color(color[0])
pen.pendown()
pen.circle(CIRCLE_DIAMETER)

# change position
pen.penup()
pen.goto(CIRCLE_DIAMETER+5, -CIRCLE_DIAMETER-5)

# write the circle
pen.pendown()
pen.color(color[1])
pen.circle(CIRCLE_DIAMETER)

# change position
pen.penup()
pen.goto(2*CIRCLE_DIAMETER+15,0)

# write the circle
pen.pendown()
pen.color(color[2])
pen.circle(CIRCLE_DIAMETER)

# change position
pen.penup()
pen.goto(3*CIRCLE_DIAMETER+20, -CIRCLE_DIAMETER)

# write the circle
pen.pendown()
pen.color(color[3])
pen.circle(CIRCLE_DIAMETER)

# change position
pen.penup()
pen.goto(4*CIRCLE_DIAMETER+30, 0)

# write the circle
pen.pendown()
pen.color(color[4])
pen.circle(CIRCLE_DIAMETER)

turtle.done()