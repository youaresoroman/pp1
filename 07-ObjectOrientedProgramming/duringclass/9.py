from class_message import Message

class Email(Message):
    def __init__(self, fromUser, toUser, topic, message=''):
        super().__init__(message)
        self.fromUser = fromUser
        self.toUser = toUser
        self.topic = topic
    def send(self):
        return f'''
Wysyłanie emaila...
\tOd: {self.fromUser}
\tDo: {self.toUser}
\tTemat: {self.topic}
\tTreść: {self.message}'''
    
m1 = Email('nowak@onet.pl','kowalski@gmail.com', 'Spotkanie w czwartek')
m1.set_message('Informuję, że nasze czwartkowe spotkanie zostało odwołane')
print(m1.send())
