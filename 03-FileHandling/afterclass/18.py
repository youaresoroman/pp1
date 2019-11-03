import re
liczby=[]

with open('numbers.txt','r') as file: 
    for x in file: 
        liczby.append(int(x))
liczby.sort()
for i in liczby:
    print(f'{i}',end=' ')