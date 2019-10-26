n=int(input('Podaj ilość szukanych liczb pierwszych: '))
liczbyPierwsze=[]
i=3

if n<1:
    print('Error')
else:
    liczbyPierwsze.append(2)
    while len(liczbyPierwsze)<n:
        for d in range(2,i):
            if i%d==0:
                break
            if d==i-1:
                liczbyPierwsze.append(i)
        i+=1

    for a in liczbyPierwsze:
        print(a,end=' ')
