import re

with open('../students.txt','r') as file:
    for line in file:
        column = re.split(',', line)
        if column[2] != 'age' and int(column[2]) < 30:
            print('{}  {}  {}'.format(column[0], column[1], column[4]))