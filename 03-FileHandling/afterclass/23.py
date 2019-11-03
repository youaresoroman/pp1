import re
suma = 0
file = open('../land.txt','r')
line = file.read()
digits = re.findall('\d', line)

for num in digits:
    suma += int(num)
    
print('Suma:{}'.format(suma))