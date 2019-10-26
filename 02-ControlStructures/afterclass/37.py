l1=int(input('Podaj pierwszą liczbę: '))
l2=int(input('Podaj drugą liczbę: '))
l3=int(input('Podaj trzecią liczbę: '))
tab=[l1,l2,l3]

for i in range(0,2):
    if tab[i+1]<tab[i]:
        (tab[i],tab[i+1])=(tab[i+1],tab[i])
        
if tab[1]<tab[0]:
    (tab[0],tab[1])=(tab[1],tab[0])

print(tab)
print(f'Mediana:  {tab[1]}')
        
    
    