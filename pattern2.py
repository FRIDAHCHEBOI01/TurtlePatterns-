import turtle

wn = turtle.Screen()
wn.bgcolor('DarkGray')

free = turtle.Turtle()
free.speed(0)
for i in range(4):
    free.forward(100)
    free.left(90)
    for j in range(1):
        free.circle(10,360)
        free.circle(-10,360)
        free.circle(-10,-360)
        
free.penup()        
free.goto(-250,-250)
free.pendown()
for i in range(4):
    free.forward(100)
    free.left(90)
    for j in range(1):
        free.circle(10,360)
        free.circle(-20,360,5)
        
free.penup()        
free.goto(250,-250)
free.pendown()
for i in range(4):
    free.forward(100)
    free.left(90)
    for j in range(1):
        free.circle(-20,360,5)
        free.circle(20,360,5)
        
free.penup()        
free.goto(200,200)
free.pendown()
for i in range(100):
    free.forward(100)
    free.left(91)
    
free.penup()        
free.goto(-200,200)
free.pendown()
k = 10
for i in range(30):
    free.left(91)
    free.forward(10+k)
    k+=10
    
    
free.penup()        
free.home()
free.forward(150)
free.pendown()

k = 1
for i in range(30):
    free.left(91)
    free.forward(10+k)
   


print(free.towards(0,0))

wn.exitonclick()










