def suma(table):
    sum = 0
    print('Tablica:', end=' ')
    for element in table:
        print(element, end=' ')
        sum += element
    print(f"\nSuma wartości: {sum}")
    
suma([4, 3, 7, 1, 3])
    