import re
numbers=[]

with open('../numbers.txt','r') as file:
    for x in file:
        numbers.append(int(x))
file.close()

with open('evennumbers.txt','w') as file1:
    for x in numbers:
        if x%2==0 and x>=0:
            file1.write(str(x)+'\n')
file1.close()