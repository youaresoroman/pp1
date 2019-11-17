def suma(liczba, n):
    if n == 0:
        return int(liczba[0])
    else:
        return int(liczba[n])+suma(liczba, n-1)
    
liczba = input('Podaj liczbę: ')
print(f'Suma cyfr liczby {liczba} wynosi {suma(liczba, len(liczba)-1)}')