import turtle
import random

k = turtle.Screen()
k.colormode(255)

t = turtle.Turtle()
t.speed(10)
t.pensize(9)
'''
writes code to draw a any sided spiral
ie. 
for i in range(100):
    t.color(random.randrange(256),random.randrange(256),random.randrange(256))
    t.forward(i*5)
    t.right(300) # the angle has to be more that 300
    t.forward(i*5)
# the code below draws a rose flower
for i in range(100):
    t.color('red')
    t.forward(i*2)
    t.right(310)
    
#Draws a weird pattern     
for i in range(100):
    t.color(random.randrange(256),random.randrange(256),random.randrange(256))
    t.circle(20,360,5)
    t.forward(10*i)
    t.right(100)
# draws an interesting pattern    
for i in range(5):    
    roof.color(random.randrange(256),random.randrange(256),random.randrange(256))
    roof.circle(rad,360)
    roof.stamp()
    rad +=20
roof.color(random.randrange(256),random.randrange(256),random.randrange(256))
roof.circle(20,360)
new = 10
for i in range(5):    
    roof.color(random.randrange(256),random.randrange(256),random.randrange(256))
    roof.circle(-10+new,360)
    roof.stamp()
    new -=20
'''
#I'm going to try to draw a face

t.up()
t.setpos(-50,0)
t.down()
t.circle(20,360)

t.up()
t.setpos(50,0)
t.down()
t.circle(20,360)
    
#okay so lets do the face
t.up()
t.setpos(-50,-60)
t.down()
t.right(45)
for i in range(60):
    t.left(2*1)
    t.forward(2*1)

#now lets do the circle face
t.up()
t.setpos(-80,0)
t.down()

t. circle(-100,360)

k.exitonclick()