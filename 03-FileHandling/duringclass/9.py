line = 'x'
with open('shoppinglist.txt','w') as file:
    while line != '':
        line = input("Podaj produkt: ")
        file.write(f"{line}\n")