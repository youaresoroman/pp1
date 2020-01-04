from class_point import Point
from math import sqrt

def distance(pon1,pon2):
    if pon1 == pon2:
        return 'Points are in same spot'
    else:
        length = sqrt((pon1.x-pon2.x)**2 + (pon1.y - pon2.y)**2)
        return length

p1 = Point(4, 3)
p2 = Point(4, 3)
p3 = Point(4, 5)
print(distance(p1,p2) + '\n',distance(p2,p3))
