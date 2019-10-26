s_p=0
s_n=0

for i in range(1,51):
    if i%2==0:
        s_p+=i
    else:
        s_n+=i
print(f'Suma liczb parzystych: {s_p} Suma liczb nieparzystych: {s_n}')