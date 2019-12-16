import random

class matrix():

    @staticmethod
    def create(x,y):
        return [[0 for w in range(x)] for h in range(y)]

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
            
    @staticmethod
    def create_unit(x):
        m = matrix.create(x,x)
        for i in range(x):
            m[i][i] = 1
        return m
    
    @staticmethod
    def fill_random(oldmatrix, m, n):
        height = len(oldmatrix)
        width = len(oldmatrix[0])
        for row in range(0, height):
            for element in range(0, width):
                oldmatrix[row][element] = random.randint(m,n)
        return oldmatrix

m1 = matrix.create_unit(5)
matrix.fill_random(m1, 1, 5)
matrix.print(m1)