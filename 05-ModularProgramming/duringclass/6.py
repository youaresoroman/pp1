import csv 
with open('../employees.csv', 'r') as file:
    reader = csv.reader(file)
    arr, age = [], []
    
    for row in reader:
        arr.append(row)
        
    print('#\tSURNAME\t\tNAME\t\tAGE\t\tMAIL')
    print('================================================')
    
    for i in range(1, len(arr)-2):
        print(str(i) + '\t' + '\t'.join(arr[i]))
        age.append(int(arr[i][2]))
        
    import statistics as st
    print(f'\nŚrednia: {st.mean(age)}')