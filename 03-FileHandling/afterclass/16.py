table = []

with open('../universities.txt', 'r') as file:
    for line in file:
        table.append(line)

table.sort()
with open('test.txt', 'w') as file:
    for name in table:
        print(name, end='')
        file.writelines(name) 