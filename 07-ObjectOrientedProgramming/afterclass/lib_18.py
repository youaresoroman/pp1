class Car():
    def __init__(self, model, number, isRented=False, mileage = 0):
        self.model = model
        self.number = number
        self.isRented = isRented
        self.mileage = mileage

    def rent(self):
        if self.isRented == False:
            self.isRented = True
            return self.isRented
        else:
            self.isRented = False
            return self.isRented
 
    def set_milage(self,mileage):
        self.mileage = mileage

    def __str__(self):
        return f'Model: {self.model} Number: {self.number} isRented: {self.isRented} Mileage: {self.mileage}'
    
    def __repr__(self):
        return f'Model: {self.model} Number: {self.number} isRented: {self.isRented} Mileage: {self.mileage}'
        
car1 = Car("BMW", "WP 33LK9")
car2 = Car("Volvo", "GSP 345LH")
print(car1)
