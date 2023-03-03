import turtle

wn = turtle.Screen()

complex = turtle.Turtle()
complex.speed(0)
complex.pensize(2)

colours = ['darkgreen','gold','olivedrab','darkcyan','royalblue','crimson']
for i in range(300):
    for item in colours:
        complex.color(item)
        complex.forward(i*5)
        complex.right(119)
        
        
        
        
wn.exitonclick()