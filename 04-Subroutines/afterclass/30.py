import random
def countNumbers(table,
                 parzyste = 0,
                 nieparzyste = 0,
                 output = [0, 0]):
    for x in table:
        if x%2==0:
            parzyste += 1
        else: nieparzyste += 1
    
    output[0] = round((parzyste/len(table))*100,2)
    output[1] = round((nieparzyste/len(table))*100,2)
    return output

numbers = []
for x in range(0, 1001):
    numbers.append(random.randrange(1, 51))

result = countNumbers(numbers)
print(f'Dla 1000 liczb losowych z przedziału <1,50>:')
print(f"Liczby parzyste: {result[0]}%")
print(f"Liczby nieparzyste: {result[1]}%")
