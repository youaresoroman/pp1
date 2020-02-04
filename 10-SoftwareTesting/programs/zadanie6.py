import random

class Macierz():
    macierz = []
    height = 0
    width = 0

    def __init__(self, x, y, filled=True):
        if filled == True:
            self.macierz = [[random.randint(0,9) for w in range(x)] for h in range(y)]
        elif filled == False:
            self.macierz = [[0 for w in range(x)] for h in range(y)]

        self.height = len(self.macierz)
        self.width = len(self.macierz[0])

    def __str__(self):
        out = ''
        for row in self.macierz:
            for element in row:
                out += f"{element} " 
            out += "\n"
        return out

    def __add__(self, other):
        newmacierz = Macierz(self.width, self.height, False)

        if (self.height == other.height and self.width == other.width):
            for row in range(0, self.height):
                for element in range(0, self.width):
                    newmacierz.macierz[row][element] = self.macierz[row][element] + other.macierz[row][element]
            return newmacierz
        else:
            return newmacierz

matrix1 = Macierz(5, 5)
matrix2 = Macierz(5, 5)

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)