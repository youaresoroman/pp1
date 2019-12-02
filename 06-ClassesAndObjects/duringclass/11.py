class TV():
    def __init__(self):
        self.stan = 'OFF'
        self.channel_no = 1
        
    def on(self):
        self.stan = 'ON'
    
    def off(self):
        self.stan = 'OFF'
        
    def status(self):
        if self.stan == 'ON':
            print(f'Odbiornik TV jest załączony, kanał {self.channel_no}')
        else:
            print('Odbiornik TV jest wyłączony')

samsung = TV()
samsung.status()
samsung.on()
samsung.status()
samsung.off()
samsung.status()