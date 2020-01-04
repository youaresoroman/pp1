class Message():
    def __init__(self,message=''):
        self.message = message
    def set_message(self,message):
        message = f'{message.capitalize()}. BYE.'
        self.message = message

m1 = Message()
print(m1.message)
m1.set_message('aorem ipsum całe te')

