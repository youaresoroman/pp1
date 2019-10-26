n=int(input('Podaj liczbe: '))
o=2

for i in range(1,2*n+1):
    if i<=n:
        print('*'*(i))
    else:
        print('*'*(i-o))
        o=o+2