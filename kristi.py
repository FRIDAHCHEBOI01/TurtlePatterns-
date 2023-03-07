import turtle

wn = turtle.Screen()
wn.bgcolor("black")

sun = turtle.Turtle()
sun.color('gold','red')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(200)
    sun.left(181)
    sun.forward(200)
    sun.left(181)  
    sun.end_fill()

sun.up()
sun.goto(-50,100)
sun.down()
sun.color('green','blue')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(150)
    sun.left(181)
    sun.forward(150)
    sun.left(181)  
    sun.end_fill()
    
sun.up()
sun.goto(-50,200)
sun.down()
sun.color('purple','pink')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(150)
    sun.left(181)
    sun.forward(150)
    sun.left(181)  
    sun.end_fill()
    
    
sun.up()
sun.goto(-100,-100)
sun.down()
sun.color('brown','orange')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(80)
    sun.left(181)
    sun.forward(80)
    sun.left(181)  
    sun.end_fill()
    
sun.up()
sun.goto(40,-240)
sun.down()
sun.color('crimson','violet')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(100)
    sun.left(181)
    sun.forward(100)
    sun.left(181)  
    sun.end_fill()
sun.up()
sun.goto(200,-200)
sun.down()
sun.color('darkmagenta','lime')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(150)
    sun.left(181)
    sun.forward(150)
    sun.left(181)  
    sun.end_fill()
    
sun.up()
sun.goto(210,150)
sun.down()
sun.color('saddlebrown','cadetblue')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(150)
    sun.left(181)
    sun.forward(150)
    sun.left(181)  
    sun.end_fill()

sun.up()
sun.goto(300,100)
sun.down()
sun.color('aqua','darkcyan')
sun.speed(0)


for i in range(100):
    sun.begin_fill()
    sun.forward(70)
    sun.left(181)
    sun.forward(70)
    sun.left(181)  
    sun.end_fill()

wn.exitonclick()