table = []

with open('../numbers.txt', 'r') as file:
    for line in file:
        table.append(int(line))

table.sort()
for number in table:
        print(number, end=' ')