from random import randrange

def rzucKostka():
    sum = 0
    print('Wyrzucone oczka:', end=' ')
    for i in range(0,3):
        random = randrange(1, 7)
        print(random, end=' ')
        sum += random
    print(f"\nSuma oczek: {sum}")

rzucKostka()