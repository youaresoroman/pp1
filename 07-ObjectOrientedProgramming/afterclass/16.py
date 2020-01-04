class Student():
    def __init__(self,first_name,last_name,index):
        self.first_name = first_name
        self.last_name = last_name
        self.index = index 
    def __repr__(self):
        return f'Imię: {self.first_name}\nNazwisko: {self.last_name}\nNr Albumu: {self.index}'
    def __eq__(self,other):
        return self.index == other.index
    def __lt__ (self,other):
        return self.index > other.index 

s1 = Student("Anna", "Tomaszewska", 141820)
s2 = Student("Wojciech", "Zbych", 201003)
s3 = Student("Maja", "Kowalska", 153202)
s4 = Student("Marek", "Migiel", 138600)

arr = [s1,s2,s3,s4]
print(sorted(arr,reverse=True))


