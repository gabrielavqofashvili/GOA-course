from turtle import *

#we want to paint a house

#step 1:draw a square
speed(10)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")

left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
left(30)
forward(20)
left(90)
forward(60)
pendown()
forward(80)
right(90)
forward(40)
right(90)
forward(80)
right(90)
forward(40)
right(180)
forward(20)
left(90)
forward(80)
right(180)
forward(40)
left(90)
forward(20)
left(180)
forward(40)
penup()
forward(2000)

exitonclick()