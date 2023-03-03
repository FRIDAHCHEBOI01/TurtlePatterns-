import turtle

wn = turtle.Screen()

complex = turtle.Turtle()
complex.speed(0)
colours = ['Deeppink','gold','purple','darkorange','limegreen','royalblue','red','brown','dimgray','black','slategray','palevioletred','mediumpurple','crimson','darkorange','darkkhaki','olivedrab']

'''
complex.up()
complex.goto(-150,-300)
complex.down()

for item in colours:
    for i in range(100):
        complex.color(item)
        complex.forward(i*2)
        complex.right(119)
'''
cp = turtle.Turtle()
cp.speed(0)

colours = ['darkred','limegreen']
for i in range(10):
    for item in colours:
        cp.color(item)
        for i in range(10):
            cp.circle(10*i,360)
        cp.right(30)

for i in range(7):
    for item in colours:
        cp.color(item)
        cp.circle(200,360)
    cp.right(30)
wn.exitonclick()
