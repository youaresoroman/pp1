def makeTable(names, counts, output = ''):
    for i in range(0, 10):
        space = 11-len(names[i])
        wartosc = int(counts[i])//3
        output += ' '*space + f'{names[i]}:' + '#'*wartosc + "\n"
    return output
        
languages = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
popularity = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

print(makeTable(languages, popularity))
