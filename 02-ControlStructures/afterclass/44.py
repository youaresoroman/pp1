limit = int(input('Podaj limit prędkości: '))
predkosc = int(input('Podaj prędkość pojazdu: '))
mandat = 0

if limit-predkosc >= -10:
    mandat = (-5)*(limit-predkosc)
else:
    mandat = 50+(-15)*(limit-predkosc+10)

print(f'Mandat: {mandat}')
