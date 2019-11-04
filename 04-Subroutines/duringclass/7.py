def printNumpad():
    for num in range(1,10):
        if num == 3 or num == 6:
            print(num)
        else:
            print(num, end=' ')

printNumpad()