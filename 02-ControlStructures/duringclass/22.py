table = [15,8,31,47,2,19]
sum=0
n=0

for i in table:
    if i%2 != 0:
        sum += i
        n += 1
    
print(f'Średnia arytmetyczna wynosi: {sum/n}')
