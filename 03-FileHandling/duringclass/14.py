import re
komunikat = 'To be, or not to be, that is the question'
cyfry = re.findall('[aeiouyAEIOUY]', komunikat)
print(cyfry)