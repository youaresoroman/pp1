from math import pi
class Math():
    @staticmethod
    def circle_area(radius):
        return f"Area: {pi*radius**2}"

    @staticmethod
    def rectangle(a,b):
        return f"Area: {a*b}"

    @staticmethod
    def triangle(a,h):
        return f"Area: {(a*h)/2}"

print(Math.circle_area(3))
print(Math.rectangle(3,4))
print(Math.triangle(3,4))