liczba = int(1)
suma = int(0)
i = int(0)

while liczba != 0:
    liczba = int(input("Podaj liczbe: "))
    if liczba != 0:
        suma += liczba
        i += 1

print(f'REZULTAT: Liczb={i}, Suma={suma}, Średnia={round(suma/i)}')
    