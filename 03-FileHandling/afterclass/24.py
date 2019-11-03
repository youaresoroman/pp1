csv = [['Imie','Nazwisko','E-mail'],
     ['Marek','Zelnik','zelnik@sed.pl'],
     ['Ewa','Maj','maje@wp.pl'],
     ['Piotr','Wyga','wygap@gop.pl']]

file = open('csv.csv','w')
for line in csv:
    for column in line:
        if column != line[-1]:
            file.write(f'{column},')
        else:
            file.write(f'{column}\n')