i=0
a=0
b=1
print(f'{a}',end=' ')
print(f'{b}',end=' ')

while i<48:
    z=b
    b=a+b
    a=z
    print(b,end=' ')
    i+=1
