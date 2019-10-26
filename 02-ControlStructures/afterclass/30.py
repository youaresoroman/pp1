pin='0805'
proba=1
while proba<5:
    u=str(input('Podaj kod PIN:'))
    if pin!=u:
        print('Kod PIN niepoprawny')
        if proba==4:
            print('Karta płatnicza zostaje zablokowana')
            proba+=1        
        else:
            proba+=1
    else:
        print('Kod PIN poprawny')
        break
