def suma(tab):
    s,x = 0,0
    while x < len(tab):
        if isinstance(tab[x], int):
            s += tab[x]
            x += 1
        else:
            s += suma(tab[x])
            x +=1
    return s            
    
print(suma([7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]))