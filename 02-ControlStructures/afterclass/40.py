import random
table = [0,0,0,0,0,0,0]

for i in range(0,100):
    table[random.randrange(1,7)]+=1

print(f'Szóstka: {table[6]}')
print(f'Piątka: {table[5]}')
print(f'Czwórka: {table[4]}')
print(f'Trójka: {table[3]}')
print(f'Dwójka: {table[2]}')
print(f'Jedynka: {table[1]}')