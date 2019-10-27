sum = 0
with open('../numbers.txt', 'r') as file:
    for line in file:
        sum += int(line)

print(f"Suma = {sum}")