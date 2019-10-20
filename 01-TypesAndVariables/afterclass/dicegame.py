import random
dice = 0
guess = 1

while dice != guess:
    guess = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
    dice = random.randint(1, 6)
    print (f"Komputer wyrzucił: {dice}")
    print (f"Zgadłeś: {dice == guess}\n")