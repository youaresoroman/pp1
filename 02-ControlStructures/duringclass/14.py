hy = float(input("Podaj wiek psa w ludzkich latach: "))
dy = int(0)

if hy > 0 and hy <= 2:
    while hy != 0:
        hy -= 1
        dy += 10.5
if hy > 2:
    hy -= 2
    dy = 21
    while hy != 0:
        hy -= 1
        dy += 4
        
print(f"Wiek psa w psich latach to {int(dy)} lata")