decimal = int(input('Podaj liczbę w systemie dziesiętnym: '))
binary = list()

print(f'{decimal}(10) = ', end='')

while decimal != 0:
    binary.append(decimal%2)
    decimal=decimal//2

binary.reverse()
for bit in binary:
    print(bit, end='')
print('(2)')