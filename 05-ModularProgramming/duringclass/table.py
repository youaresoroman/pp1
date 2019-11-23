import shapes

maxsize = 200
size = maxsize
while size != 0:
    shapes.drawSquare(0, 0, size)
    shapes.drawSquare(maxsize-size, -(maxsize-size), size)
    size -= maxsize/4