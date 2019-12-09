class Student():
    counter = 100000
    
    def __init__(self):
        self.uczelnia = 'UEK Kraków'
        
    def new(self, name, surname, study):
        self.album = self.counter
        self.name = name
        self.surname = surname
        self.album = self.counter
        self.study = study
        self.counter += 1
        
    def __str__(self):
        out = f"Name: {self.name}"
        return f"{out}"
    
students = Student()
students.new('Ivan', 'Ivanov', 'Informatics')
print(students)