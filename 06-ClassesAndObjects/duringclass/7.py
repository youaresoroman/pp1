class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)

uek = University()
uek.print_name()