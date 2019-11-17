def reverse(tab,
            new_tab = []):
    for x in range(0, len(tab)):
        new_tab.append(tab[-x-1])
    
    return new_tab

print(reverse([2, 5, 4, 1, 8, 7, 4, 0, 9]))