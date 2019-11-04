def potega(x, n):
    
    if n==0:
        return 1
    if n==1:
        return x
    if n > 1:
        return x * potega(x, n-1)

print("5**3 =", potega(5, 3))