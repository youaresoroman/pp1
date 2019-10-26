import random

for i in range(0,20):
    if i != 19:
        print(random.randint(-20,-4),end=', ')
    if i == 19:
        print(random.randint(-20,-4))