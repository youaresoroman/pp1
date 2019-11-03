tab = [32, 16, 5, 8, 24, 7]

with open('tab13.txt','w') as file:
    for x in tab:
        file.write(str(x)+'\n')