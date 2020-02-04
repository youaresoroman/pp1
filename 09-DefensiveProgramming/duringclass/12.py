wiek = '25'
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
    print(f'Masz {wiek} lat')
elif wiek>=0 or wiek>=120:
    raise ValueError('Wiek powinien być liczbą dodatnią, mniejszą od 120!')
    print(f'Masz {wiek} lat')