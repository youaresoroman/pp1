import re

komunikat = 'wtorek -23C, środa - 17C, czwartek - 25C'
numbers = re.findall('\d{2}',komunikat)
sum = 0

for number in numbers:
    sum+=int(number)
    
print(f'Średnia temp: { round(sum/len(numbers),2)}')