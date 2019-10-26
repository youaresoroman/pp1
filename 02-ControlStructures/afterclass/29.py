tab=[15,8,31,47,2,19]
print('tab: ',end=' ')
for i in tab:
    if i!=(tab[len(tab)-1]):
        print(i,end=" ")
    else:
        print(i,end="\n")

print('tab in reverse: ',end=' ')
for i in range(1,len(tab)+1):
    print(tab[len(tab)-i],end=' ')