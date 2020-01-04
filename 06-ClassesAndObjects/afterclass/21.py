from statistics import median
class Statystyka():
    
    def __init__(self,zbior):
        self.zbior = zbior
    
    def __str__(self):
        return f'Zbiór: {self.zbior}'
    
    def add(self, number):
        self.zbior.append(number)
    
    def maxval(self):
        return f'Max: {max(self.zbior)}'
    
    def minval(self):
        return f'Min: {min(self.zbior)}'
    
    def srednia(self):
        return f'Srednia: {sum(self.zbior)/len(self.zbior)}'
    
    def mediana(self):
        return f'Mediana: {median(self.zbior)}'
    

arr = Statystyka([1,2,3,4,5,6])
print(arr)
arr.add(9)
print(arr)
print(arr.maxval())
print(arr.minval())
print(arr.mediana())

