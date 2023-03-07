import turtle

wn = turtle.Screen()
wn.bgcolor("black")

mine = turtle.Turtle()
mine.speed(0)
mine.color("crimson",'salmon')

mine.begin_fill()
for i in range(100):
    mine.forward(300)
    mine.left(119)
mine.end_fill()