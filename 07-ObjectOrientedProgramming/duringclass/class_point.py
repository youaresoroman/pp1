class Point():
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def __str__(self): 
        return f'P({self.x},{self.y})'
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

p1 = Point(4,3)
p2 = Point(4,3)
p3 = Point(4,5)
print(f'''
{p1 == p2}
{p3 == p2}''')