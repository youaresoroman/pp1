table = [32, 16, 5, 8, 24, 7]

file = open('output.txt','w')
for number in table:
    file.write(f"{number}\n")