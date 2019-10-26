a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

import math

delta=b*b-4*a*c
print(f'Równanie kwadratowe: {a}x^2+{b}x+{c}=0')

if delta>=0:
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    if x1!=x2:
        print(f'Pierwiastki równania: x1 = {x1}  x2 = {x2}')
    else:
        print(f'Pierwiastek równania: x = {x1}')
else:
    print('Pierwiastek nie istnieje')