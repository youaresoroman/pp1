def jestImie(imie, imiona):
    print(f"Imie: {imie}")
    print("Imiona:", end=' ')
    
    for element in imiona:
        print(element, end=' ')
        if element == imie:
            print("\nRezultat: imię zawarte jest w wykazie imion")
            return
        
    print("\nRezultat: imię zawarte nie jest w wykazie imion")
    
jestImie('Wojtek', ['Janek', 'Ania', 'Wojtek', 'Zosia'])