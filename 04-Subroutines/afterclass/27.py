text = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'

def count(a, text, count = 0):
    for x in text.lower():
        if x == a: count += 1
    return count

letter = input('Podaj samogłoskę: ')
print(f"Samogłoska '{letter}' występuje w tekście {count(letter, text)} razy.")