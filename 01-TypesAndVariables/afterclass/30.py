row = [12, 6, 4, 9, 3]

for x in row:
    column = str()
    i = 0
    while i != x:
        column += '*'
        i += 1
    print(f"{x}: {column}")