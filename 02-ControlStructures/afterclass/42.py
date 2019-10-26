a=int(input('Podaj liczbę: '))
b=int(input('Podaj liczbę: '))

if b==0:
    print('Dzielenie przez 0!')
else:
    print(f'{a}/{b} = {round(a/b,4)}')