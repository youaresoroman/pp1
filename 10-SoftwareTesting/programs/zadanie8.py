#dodaj(sala) – dodaje salę do wykazu sal
#• liczba_sal() – zwraca liczbę sal
#• razem_miejsc() – zwraca liczbę miejsc dostępnych we wszystkich salach
#• liczba_miejsc(nazwa_sali) – zwraca liczbę miejsc dla sali o podanej nazwie; w przypadku, gdy sala o podanej nazwie nie występuje w wykazie sal, metoda zwraca wartość 0
#• liczba_sal_przedzial(od,do) – zwraca liczbę sal, które posiadają liczbę miejsc w podanym przedziale <od,do>.
#Utwórz klasy Sala oraz Sale


class Sala():
    def __init__(self, name, seats):
       self.name = name
       self.seats = seats
       
class Sale():
    sale = []
    count = 0
    
    def dodaj(self, Sala):
        self.sale.append(Sala)
        self.count += 1
        
    def print_obj (self, id):
        print(self.sale[id].name)
        
    def liczba_sal(self):
        return self.count
    
    def razem_miejsc(self):
        sum = 0
        for sala in self.sale:
            sum += sala.seats
        return sum
    
    def liczba_miejsc(self, name):
        for sala in self.sale:
            if name == sala.name:
                return (sala.seats)
    
obj = Sale()
obj.dodaj(Sala("Nowa Aula", 80))
obj.dodaj(Sala("Hala sportowa", 500))
obj.dodaj(Sala("Lab. komputerowe 115", 35))
obj.dodaj(Sala("Sala 053", 45))
obj.dodaj(Sala("Sala G", 70))
print(obj.razem_miejsc())
print(obj.liczba_miejsc("Nowa Aula"))        