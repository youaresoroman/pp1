tab=str(input('Podaj ciąg znaków: '))
names = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']

for i in range(0, len(tab)):
    
    print(f"{names[int(tab[i])]}", end = ' ')
