import turtle
import random

wn = turtle.Screen()

colours = ['hotpink','gold','silver']

t = turtle.Turtle()
t.up()
t.setpos(0,300)
t.down()
t.speed(0)

for i in range(12):
    for k in colours:
        t.color(k)
        t.begin_fill()
        t.circle(20,360,6)
        t.right(10)
        t.forward(40)
        t.end_fill()
# To draw the outer circle     
t.left(90)
t.forward(40)
t.right(90)
for i in range(36):
    t.right(10)
    t.forward(40)




wn.exitonclick()