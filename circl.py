color = input('Enter number')
import turtle
import random

wn = turtle.Screen()
wn.colormode(255)
t = turtle.Turtle()
t.speed(0)
t.pensize(6)

'''
for i in range(100):
    t.forward(2*i)
    t.right(80)

for i in range(100):
    t.circle(80,360)
    t.right(91+i)
'''
for i in range(50):
    t.color(random.randrange(256), random.randrange(256), random.randrange(256))
    t.circle(20,360)
    t.right(80*i)

wn.exitonclick()