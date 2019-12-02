class TV():
    def __init__(self):
        self.stan = 'OFF'
        
    def on(self):
        self.stan = 'ON'
    
    def off(self):
        self.stan = 'OFF'
        
    def status(self):
        print(self.stan)

samsung = TV()
samsung.status()
samsung.on()
samsung.status()
samsung.off()
samsung.status()