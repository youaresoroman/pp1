import random

class Macierz():

    @staticmethod
    def create(x, y, filled=True):
        if filled == True:
            return [[random.randint(0,9) for w in range(x)] for h in range(y)]
        elif filled == False:
            return [[0 for w in range(x)] for h in range(y)]

    @staticmethod
    def dimentions(matrix):
        return {"height": len(matrix), "width": len(matrix[0])}
    
    @staticmethod
    def sum(matrix1, matrix2):
        dimensionsM1 = Macierz.dimentions(matrix1)
        dimensionsM2 = Macierz.dimentions(matrix2)
        height = dimensionsM1['height']
        width = dimensionsM1['width']

        if (dimensionsM1 == dimensionsM2):
            newmatrix = Macierz.create(width, height, False)

            for row in range(0, height-1):
                for element in range(0, width-1):
                    newmatrix[row][element] = matrix1[row][element] + matrix2[row][element]
            return newmatrix
        else:
            return Macierz.create(width, height)

matrix1 = Macierz.create(5, 6)
matrix2 = Macierz.create(5, 6)
print(f"{matrix1}\n{matrix2}")
print(f"{Macierz.sum(matrix1, matrix2)}")