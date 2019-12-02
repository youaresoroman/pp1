class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    def set_name(self, new_name):
        self.name = new_name

uek = University()
uek.print_name()
uek.set_name("UJ")
uek.print_name()