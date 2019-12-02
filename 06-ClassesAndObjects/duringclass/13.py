class TV():
    def __init__(self):
        self.stan = 'OFF'
        self.channel_no = 1
        self.channels = []
        
    def on(self):
        self.stan = 'ON'
    
    def off(self):
        self.stan = 'OFF'
        
    def status(self):
        if self.stan == 'ON':
            print(f'Odbiornik TV jest załączony, kanał {self.channel_no}')
        else:
            print('Odbiornik TV jest wyłączony')
    def set_channel(self, new_channel_no):
        self.channel_no = int(new_channel_no)
        
    def set_channels(self, channels_list):
        self.channels = channels_list
    
    def show_channels(self):
        i = 1
        for channel in self.channels:
            print(f'{i}. {channel}')
            i += 1

samsung = TV()
samsung.status()
samsung.on()
samsung.status()
samsung.show_channels()
samsung.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox'])
samsung.show_channels()
samsung.off()