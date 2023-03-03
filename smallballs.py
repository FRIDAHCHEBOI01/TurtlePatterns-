import turtle

wn = turtle.Screen()
wn.bgcolor('black')

turt = turtle.Turtle()
turt.speed(0)
turt.color('mediumseagreen')

for i in range(35):
    turt.begin_fill()
    turt.circle(10,360)
    turt.end_fill()
    turt.right(10)
    turt.up()
    turt.forward(30)
    turt.down()
turt.shape('circle')
    
for i in range(30):
    turt.left(30)
    turt.up()
    turt.forward(40)
    turt.down()
    turt.stamp()
    
wn.exitonclick()