p = lambda x:x%2==0

for x in filter(p, [1,2,3,4,5,6,7,8]):
    print(x, end=' ')


