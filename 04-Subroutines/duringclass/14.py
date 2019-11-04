def wystepuje(testnum, table):
    status = False
    print(f"Liczba: {testnum}")
    print("Tablica:", end=' ')
    for element in table:
        print(element, end=' ')
        if element == testnum:
            status = True
    if status:
       print("\nRezultat: Podana liczba występuje w tablicy") 
    else:
       print("\nRezultat: Podana liczba nie występuje w tablicy")
    
wystepuje(23, [15, 38, 7, 23, 14])