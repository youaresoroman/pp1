def jest(search, start, end):
    if type(search) is int and type(start) is int and type(end) is int:
        if search >= start and search <= end:
            return True
    return False
      
liczba = input('Podaj liczbę: ')
range = input('Podaj zakres <x,y>: ')
range = range.split(",")

if jest(int(liczba), int(range[0]), int(range[1])):
    print('Liczba {} mieści się w przedziale <{},{}>.'.format(liczba, range[0], range[1]))
else:
    print('Liczba {} nie mieści się w przedziale <{},{}>.'.format(liczba, range[0], range[1]))