import turtle

wn = turtle.Screen()
wn.bgcolor('lavender')

love =turtle.Turtle()
love.speed(0)
love.pensize(3)
love.shape('circle')



x = 100
y = 100
z = 15
colours = ['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'BlanchedAlmond',
'BlueViolet', 'CadetBlue', 'Chocolate', 'CornflowerBlue', 'Coral', 'Crimson', 'Cyan', 'DarkCyan',
'DarkGoldenRod', 'DarkGray', 'DarkKhaki', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid','Darkred', 'Darksalmon',
'Darkseagreen', 'Darkslate blue', 'darkslategrey', 'DarkTurquoise', 'Deep pink', 'Deep blue sky', 'Dimgray',
'Dodgerblue', 'Firebrick', 'floralwhite', 'gold', 'goldenrod', 'gray', 'greenyellow','indianred', 'ivory', 'lavender',
'khaki', 'lemonchiffon', 'lightcoral', 'lightblue', 'lightcoral', 'lightcyan', 'lightsalmon', 'lightseagreen',
'lightpink', 'orange', 'orangered', 'orchid', 'palevioletred', 'peru', 'pink', 'plum', 'rebeccapurple', 'powderblue',
'rosybrown', 'saddle brown', 'royalblue', 'thistle', 'teal', 'tan']

'''
for i in range(20):
    love.color(colours[i])
    love.penup()
    love. forward(50)
    love.pendown()
    love.stamp()
 '''   
'''for j in range(6):
    love.color(colours[i])
    for k in range(6):
        for l in range(6):
            love.goto(k * x - 300 + l, j * x - 300,)
            love.stamp()
 '''
love.speed(10)
startpoint = 0
for col in range(6):
    love.goto(0+col*50,0)
    for k in range(6):
        love.stamp()
        love.penup()
        love.goto(k*20,k*12)
        love.pendown()
     
    
    
   
    
        
    
    




wn.exitonclick()