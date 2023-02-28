# Something that is personally meaningfull to me
import turtle
import random

wn = turtle.Screen()
wn.colormode(255)
colors = ['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Bisque', 'BlanchedAlmond', 'BlueViolet', 'CadetBlue', 'Chocolate', 'CornflowerBlue', 'Coral', 'Crimson', 'Cyan', 'DarkCyan',
'DarkGoldenRod', 'DarkGray', 'DarkKhaki', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid','Darkred', 'Darksalmon',
'Darkseagreen', 'Darkslate blue', 'darkslategrey', 'DarkTurquoise', 'Deep pink', 'Deep blue sky', 'Dimgray',
'Dodgerblue', 'Firebrick', 'floralwhite', 'gold', 'goldenrod', 'gray', 'greenyellow','indianred', 'ivory', 'lavender',
'khaki', 'lemonchiffon', 'lightcoral', 'lightblue', 'lightcoral', 'lightcyan', 'lightsalmon', 'lightseagreen',
'lightpink', 'orange', 'orangered', 'orchid', 'palevioletred', 'peru', 'pink', 'plum', 'rebeccapurple', 'powderblue',
'rosybrown', 'saddle brown', 'royalblue', 'thistle', 'teal', 'tan']
dist = 20
'''for i in range(10):
    polt = turtle.Turtle()
    polt.shape('circle')
    polt.stamp()
    polt.left(10 + dist)
    polt.forward(20+dist)
    dist +=40
    
for j in range(5):
    polt = turtle.Turtle()
    polt.shape('circle')
    polt.left(5+dist)
    for i in range(5):
        polt.stamp()
        polt.forward(2+dist)
        dist += 5    '''
#I love the above code
#So I will be creating the Ashesi logo, because Ashesi means alot to me

# the roof
roof = turtle.Turtle()
roof.color(random.randrange(256),random.randrange(256),random.randrange(256))
roof.shape('circle')
roof.speed(0)

roof.pensize(12)
roof.penup()
roof.setpos(-150, 0)
roof.pendown()
roof.left(30)
roof.forward(150)
roof.left(-60)
roof.forward(150)

# the dot under the roof
roof.penup()
roof.setpos(-20,20)
roof.pendown()
roof.begin_fill()
roof.circle(10,360)
roof.end_fill()

# the upper part of the stool slightly curved
roof.up()
roof.setpos(-120,0)
roof.down()
roof.circle(200,60)
# the stands of the stool
roof.up()
roof.setpos(-80,-17)
roof.down()
roof.right(120)
roof.forward(90)

roof.up()
roof.setpos(-20,-25)
roof.down()
roof.forward(80)

roof.up()
roof.setpos(40,-20)
roof.down()
roof.forward(86)
# the lower curve of the stool
roof.up()
roof.setpos(-130,-110)
roof.down()
roof.left(90)
roof.forward(220)

roof.up()
roof.goto(-20,-200)
roof.down()
rad = 220
roof.pensize(10)
roof.circle(200,360)

roof.up()
roof.setpos(0,-300)
roof.hideturtle()
roof.write('I LOVE ASHESI AMAZINGLY MUCH!!!', move=True,align='center',font=("TimesNewRoman",30,("bold","normal")))


t = turtle.Turtle()
#I'm going to try to draw a face
#now lets do the circle face
t.up()
t.setpos(280,300)
t.down()
t.begin_fill()
t.color(random.randrange(256),random.randrange(256),random.randrange(256))
t. circle(-100,-360)
t.end_fill()
#eyes
t.color('black')
t.hideturtle()
t.pensize(10)
t.up()
t.setpos(200,200)
t.down()
t.circle(20,360)

t.up()
t.setpos(250,200)
t.down()
t.circle(20,360)
    

#smile
t.up()
t.setpos(200,180)
t.down()
t.right(45)
for i in range(60):
    t.left(2*1)
    t.forward(2*1)



        

wn.exitonclick()