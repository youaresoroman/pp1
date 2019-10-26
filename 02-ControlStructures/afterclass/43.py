tab=[]

tab.append(int(input('Podaj pierwszą liczbę: ')))
tab.append(int(input('Podaj drugą liczbę: ')))
tab.append(int(input('Podaj trzecią liczbę: ')))

for i in range(0,2):
    if tab[i+1]<tab[i]:
        (tab[i],tab[i+1])=(tab[i+1],tab[i])
        
if tab[1]<tab[0]:
    (tab[0],tab[1])=(tab[1],tab[0])
    
print(f'Liczby w kolejności rosnącej:{tab[0]},{tab[1]},{tab[2]}')