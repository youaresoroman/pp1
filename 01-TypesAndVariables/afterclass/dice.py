import random
dice = list()
i = 0

while i != 3:
    dice.append(random.randint(1, 6))
    i += 1

sum = dice[0] + dice[1] + dice[2]

print(dice, sum)