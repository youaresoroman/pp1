def fib(n):
    if n > 2: 
        return fib(n-2)+fib(n-1)
    elif n == 2:
        return fib(1)+1
    elif n == 1:
        return 0

for x in range(1, 20):
    print(fib(x), end=' ')