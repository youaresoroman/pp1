table = []
sum = 0
file_r = open('../numbersinrows.txt', 'r')
for line in file_r:
    line = line.strip('\n')
    line = line.split(",")
    
    for number in line:
        table.append(number)
        sum += int(number)

print(f"count:{len(table)}, sum:{sum}")
file_r.close()