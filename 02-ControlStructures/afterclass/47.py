monety = [1,2,5]
ilosc = [0,0,0]
kwota = int(input('Podaj kwotę w zł: '))

if kwota <= 0:
    print('Błąd')
    
else:
    for i in range(2,-1,-1):
        if kwota/monety[i] >= 1:
            ilosc[i] = kwota//monety[i]
            kwota -= ilosc[i]*monety[i]
    print(f'5zł - {ilosc[2]} szt')
    print(f'2zł - {ilosc[1]} szt')
    print(f'1zł - {ilosc[0]} szt')
