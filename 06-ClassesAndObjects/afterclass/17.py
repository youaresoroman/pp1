from math import gcd
class Div():
    def __init__(self,upper,lower):
        self.upper = upper
        self.lower = lower 
    def displayDiv(self):
        return f'{self.upper}/{self.lower}'
    def shortDiv(self):
        x = gcd(self.upper,self.lower)
        self.upper /= x
        self.lower /= x
        
newDiv = Div(10,15)
print(newDiv.displayDiv())
newDiv.shortDiv()
print(newDiv.displayDiv())