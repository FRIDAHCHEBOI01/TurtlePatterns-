import turtle

wn = turtle.Screen()

t = turtle.Turtle()
colours = ['hotpink','yellow','silver']
t.pensize(2)
t.speed(0)
t.setpos(0,300)
sub = 0
x= 0
y= 300
#This is the first way to do it
'''
#t.begin_fill()
t.color('hotpink')
for i in range(18):
    t.right(90-sub)
    t.forward(240)
    t.up()
    t.setheading(0)
    t.setpos(x,y)
    t.down()
    sub += 10
    y= y- 40

    
t.setheading(180)
sub = 0
x= 0
y= 300

for i in range(19):
    t.right(90+sub)
    t.forward(240)
    t.up()
    t.setheading(0)
    t.setpos(x,y)
    t.down()
    sub += 10
    y= y- 40
#t.end_fill()
'''
#this is the second way to do it
#right upper part
x1= 20
y1= 0

x2 = 0
y2 = 300

for i in range(17):
    t.goto(x1,y1)
    t.up()
    t.goto(x2,y2)
    t.down()
    y2-=20
    x1 +=20
#left upper part
x1= 0
y1= 0

x2 = 0
y2 = 300

for i in range(17):
    t.goto(x1,y1)
    t.up()
    t.goto(x2,y2)
    t.down()
    y2-=20
    x1 -=20
print(t.pos())
t.goto(0,0)

#left lower part
x1= 20
y1= 0

x2 = 0
y2 = -300

for i in range(17):
    t.goto(x1,y1)
    t.up()
    t.goto(x2,y2)
    t.down()
    y2+=20
    x1 -=20
print(t.pos())
t.goto(0,0)

#right lower part
x1= 0
y1= 0

x2 = 0
y2 = -300

for i in range(17):
    t.goto(x1,y1)
    t.up()
    t.goto(x2,y2)
    t.down()
    y2+=20
    x1 +=20
print(t.pos())
t.goto(0,0)



wn.exitonclick()
    