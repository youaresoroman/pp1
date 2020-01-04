class Kontakt ():

    def __init__(self,nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon
    def __repr__(self):
        return f'Name: {self.nazwa} Email: {self.email} Telefon: {self.telefon}'

class ListaKontakt():
    
    arrOfKontakt = []
    @classmethod
    def add_kontakt(cls,kontakt):
        cls.arrOfKontakt.append(kontakt)
    @classmethod
    def show_kontakt_list(cls):
        return print(cls.arrOfKontakt)

contacts = []
contacts.append(Kontakt('Kowalski Jan', 'jank@onet.pl', '555234000'))
contacts.append(Kontakt('Borek Patrycja', 'bp@o2.pl', '232000199'))
contacts.append(Kontakt('Maj Piotr', 'maj@google.pl', '222999100'))
contacts.append(Kontakt('Adamczyk Anna', 'ada@poczta.pl', '100200300'))

for contact in contacts:
    ListaKontakt.add_kontakt(contact)
ListaKontakt.show_kontakt_list()