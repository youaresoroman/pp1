suma = 0
with open('../numbers.txt','r') as file:
    for x in file:
        suma+=int(x)
        
print(suma)
