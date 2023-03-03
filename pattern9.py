import turtle


wn = turtle.Screen()
'''
hex = turtle.Turtle()
hex.speed(0)
hex.up()
hex.goto(-300,250)
hex.down()

for k in range(18):
    hex.circle(30,360,6)
    hex.right(20)

hex.up()
hex.goto(-200,200)
hex.down()
for i in range(6):
    hex.forward(30)
    hex.left(60)

hex.up()
hex.goto(-80,200)
hex.down()
colours = ['gold','hotpink','silver','orange','yellow']
p = 0
for k in range(5):
    hex.color(colours[p])
    for i in range(6):
        for i in range(3):
            hex.forward(20*k/2)
            hex.left(120)
        hex.left(60)
    p +=1

spiral = turtle.Turtle()
spiral.speed(0)
spiral.up()
spiral.goto(0,300)
spiral.down()


for i in range(30):
    spiral.forward(2*i)
    spiral.left(90)
    
    
spiral.up()
spiral.goto(50,260)
spiral.down()


for item in colours:
    spiral.color(item)
    spiral.circle(20,360)
    spiral.forward(10)

spiral.up()
spiral.goto(150,260)
spiral.down()

for i in range(9):
    for item in colours:
        spiral.color(item)
        spiral.circle(25,360)
        spiral.right(10)

spiral.up()
spiral.goto(300,260)
spiral.down()
spiral.color('black')

for i in range(20):
    for i in range(4):
        spiral.forward(60)
        spiral.right(90)
    spiral.right(18)
'''

complex = turtle.Turtle()
complex.speed(0)
colours = ['Deeppink','gold','purple'] #'darkorange','limegreen'

complex.up()
complex.goto(-300,0)
complex.down()

for i in range(15):
    for item in colours:
        complex.color(item)
        complex.circle(90,360,3)
        complex.right(10)
  
complex.up()
complex.goto(0,0)
complex.down()

for i in range(720):
    for item in colours:
        complex.color(item)
        complex.forward(i*2)
        complex.right(119)
    

wn.exitonclick()