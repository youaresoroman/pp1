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
        
maxsize = 200
size = maxsize
while size != 0:
    drawSquare(0, 0, size)
    drawSquare(maxsize-size, -(maxsize-size), size)
    size -= maxsize/4