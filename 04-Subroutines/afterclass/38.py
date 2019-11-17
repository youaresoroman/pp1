def wielkie(ciag,
            wynik = []):
    for x in ciag:
        if ord(x) > 64 and ord(x) < 91:
            wynik.append(x)
    return wynik

for letter in wielkie(input('Podaj ciąg liter: ')):
    print(letter, end='')