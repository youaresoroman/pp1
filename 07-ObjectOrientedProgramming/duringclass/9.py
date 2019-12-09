class Message():
    def __init__(self):
        self.message = ''
        
    def set_message(self, message):
        self.message = message[0].upper() + message[1:len(message)].lower() + " BYE."
    
    def __str__(self):
        return f"{self.message}"

class SMS(Message):
    def __init__(self):
        
    
message = Message()
message.set_message('swlSET')