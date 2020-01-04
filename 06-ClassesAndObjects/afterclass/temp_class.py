class Temp():
    def __init__(self):
        pass
    def checkTemp(self,tempC):
        self.temp = tempC
        if self.temp >= 41:
            return f'{self.temp} - Stan zagrożenia życia'
        elif self.temp >= 37:
            return f'{self.temp} - Gorączka'
        else:
            return self.temp