import turtle

wn = turtle.Screen()
wn.bgcolor('black')

turt = turtle.Turtle()
turt.speed(0)
turt.color('white')

for i in range(400):
    turt.forward(i*2)
    turt.left(119)
    
    
    
    
    
wn.exitonclick()