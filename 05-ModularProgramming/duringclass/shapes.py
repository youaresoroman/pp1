import turtle as turtle

def drawSquare(x, y, n):
    turtle.color('red', 'yellow')
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(n)
        turtle.right(90)