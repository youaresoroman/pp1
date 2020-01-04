from lib_18 import car1, car2, Car

class CarRent():
    car_list = []
    @classmethod
    def showAllCars(cls):
        return f"All cars: {cls.car_list}"
    @classmethod
    def addCar(cls, car):
        if car in cls.car_list:
            return "This car is already in"
        else:
            cls.car_list.append(car)
            return f"Added car {car}" 
    @classmethod 
    def showNotRentedList(cls):
        return f'Free cars: {list(filter(lambda x: not x.isRented ,cls.car_list))}'

    @classmethod
    def showRentedList(cls):
        return f'Rented cars: {list(filter(lambda x: x.isRented ,cls.car_list))}'


print(car1)
print(CarRent.addCar(car1))
print(CarRent.addCar(car2))
print(CarRent.showNotRentedList())
print("RENTING VOLVO")
car2.rent()
print(CarRent.showRentedList())
print(CarRent.showAllCars())
