import turtle

wn = turtle.Screen()
wn.bgcolor('black')

sphex = turtle.Turtle()
sphex.color('crimson')
sphex.pensize(3)
sphex.left(20)
sphex.speed(0)

colours = ['Deeppink','gold','olivedrab']
k=0

for i in range(150):
    for item in colours:
        sphex.color(item)
        sphex.forward(i*3)
        sphex.right(59)
        k+=1
        
    
    
wn.exitonclick()