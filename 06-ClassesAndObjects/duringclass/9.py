class University():
    def __init__(self):
        self.name = 'UEK'
        self.fullname= 'Uniwersytet Ekonomiczny w Krakowie'
        
    def set_name(self, new_name):
        self.name = new_name
        
    def print_name(self):
        print(self.name)
        
    def set_fullname(self, fullname):
        self.fullname = fullname
        
    def print_fullname(self):
         print(self.fullname)
    
uek = University()
uek.print_fullname()
uek.set_fullname("Uniwersytet Jagielonski w Krakowie")
uek.print_fullname()