from turtle import *


#we want to paint a house

#step 1:  draw a square

shape("turtle")

width(7)

color("purple")

forward (200)
left (90)
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square

#drawing a door

forward(65)
color("yellow")
begin_fill()
left(90)
forward(90)
right(90)
forward(65)
right(90)
forward(90)
end_fill()

#end of door

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(10,110)
pendown()

color("blue")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(190,110)
pendown()

color("blue")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()