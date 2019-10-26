table=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']

table_count: int = len(table)
current_len: int = 0
longest_id: int  = 0
temporary_len: int  = 0

for current_id in range(0, table_count):
    temporary_len = len(table[current_id])
    
    if temporary_len > current_len:
        longest_id = current_id
        current_len = temporary_len


print(f'Najdłuższe imię: {table[longest_id]}')