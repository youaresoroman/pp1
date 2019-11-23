def znakiWspak(string):
    return string[::-1]

def sepratedByspace(string):
    return ' '.join(string)

def upperletters(string,
                 output = ''):
    for word in string.split(' '):
        output += word.capitalize() + ' '
    return output