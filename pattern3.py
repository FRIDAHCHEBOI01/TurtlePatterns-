import turtle


wn = turtle.Screen()
wn.bgcolor('thistle')

man = turtle.Turtle()
colors = ['goldenrod', 'gray', 'greenyellow','indianred', 'ivory', 'lavender',
'khaki', 'lemonchiffon', 'lightcoral', 'lightblue', 'lightcoral', 'lightcyan', 'lightsalmon', 'lightseagreen',
'lightpink', 'orange', 'orangered', 'orchid', 'palevioletred', 'peru']
man.speed(0)
for color in colors:
    man.color(color)
    for k in range(4):
        man.left(90)
        man.forward(100)
        man.left(100)
     
man.penup()        
man.forward(150)
man.pendown()     
man.speed(0)
for color in colors:
    man.color(color)
    for k in range(4):
        man.left(90)
        man.forward(100)
        man.left(100)
        
man.penup()        
man.forward(-150)
man.pendown()     
man.speed(0)
for color in colors:
    man.color(color)
    for k in range(4):
        man.left(90)
        man.forward(100)
        man.left(100)