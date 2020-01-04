class Phone(object):
    
    def __init__(self, model, size, year, favcontact=None):
        self.model = model
        self.size = size 
        self.year = year
        self.favcontact = favcontact
    def __str__(self):
        return f'Model: {self.model}\nSize: {self.size}\nYear: {self.year}'
    def how_old(self):
        return 2019 - self.year
    def call(self):
        return f'Calling: {self.favcontact}'


p1 = Phone("Galaxy s8", "148.9 x 68.1 x 8.0 mm", 2017, "Harry Potter")
p2 = Phone("Iphone 11", "150.9 x 75.7 x 8.3 mm", 2019, "Garry Oldman")
print(p1.how_old())
print(p1.call())
print(p2.how_old())
print(p2.call())