import turtle

wn = turtle.Screen()
wn.bgcolor('black')

colours = ['gold','white','crimson','orange','green','blue']

p10 = turtle.Turtle()
p10.speed(0)
p10.pensize(2)
k = 0

for i in range(50):
    p10.color('red')
    p10.circle(i,360,6)
    p10.forward(5)

p11 = turtle.Turtle()
p11.speed(0)
p11.pensize(2)
p11.left(10)
for i in range(50):
    p11.color('gold')
    p11.circle(i,360,6)
    p11.forward(5)
    
p11 = turtle.Turtle()
p11.speed(0)
p11.pensize(2)
p11.left(20)
for i in range(50):
    p11.color('gold')
    p11.circle(i,360,6)
    p11.forward(5)
    
p11 = turtle.Turtle()
p11.speed(0)
p11.pensize(2)
p11.left(40)
for i in range(50):
    p11.color('hotpink')
    p11.circle(i,360,6)
    p11.forward(5)
    
p11 = turtle.Turtle()
p11.speed(0)
p11.pensize(2)
p11.left(60)
for i in range(50):
    p11.color('hotpink')
    p11.circle(i,360,6)
    p11.forward(5)    
    
p11 = turtle.Turtle()
p11.speed(0)
p11.pensize(2)
p11.left(80)
for i in range(50):
    p11.color('limegreen')
    p11.circle(i,360,6)
    p11.forward(5)
x=100    
for i in range(2):
    p11 = turtle.Turtle()
    p11.speed(0)
    p11.pensize(2)
    p11.left(x)
    for i in range(50):
        p11.color('royalblue')
        p11.circle(i,360,6)
        p11.forward(5)
    x+=20
x= 140    
for i in range(2):
    p11 = turtle.Turtle()
    p11.speed(0)
    p11.pensize(2)
    p11.left(x)
    for i in range(50):
        p11.color('tan')
        p11.circle(i,360,6)
        p11.forward(5)
    x = x+20

x= 180   
for i in range(2):
    p11 = turtle.Turtle()
    p11.speed(0)
    p11.pensize(2)
    p11.left(x)
    for i in range(50):
        p11.color('darkgreen')
        p11.circle(i,360,6)
        p11.forward(5)
    x = x+20
x= 220    
for i in range(2):
    p11 = turtle.Turtle()
    p11.speed(0)
    p11.pensize(2)
    p11.left(x)
    for i in range(50):
        p11.color('cyan')
        p11.circle(i,360,6)
        p11.forward(5)
    x = x+20

x= 260    
for i in range(2):
    p11 = turtle.Turtle()
    p11.speed(0)
    p11.pensize(2)
    p11.left(x)
    for i in range(50):
        p11.color('white')
        p11.circle(i,360,6)
        p11.forward(5)
    x = x+20

x= 300    
for i in range(2):
    p11 = turtle.Turtle()
    p11.speed(0)
    p11.pensize(2)
    p11.left(x)
    for i in range(50):
        p11.color('purple')
        p11.circle(i,360,6)
        p11.forward(5)
    x = x+20
    
p11 = turtle.Turtle()
p11.speed(0)
p11.pensize(2)
p11.left(340)
for i in range(50):
    p11.color('red')
    p11.circle(i,360,6)
    p11.forward(5)
wn.exitonclick()