def wyznaćCenuBrutto(netto):
    if type(netto) == int or type(netto) == float and netto > 0:
        if netto > 0:
            return round(netto*0.23 + netto, 2)
        else:
           raise ValueError('netto musi byc dodatną liczbą!') 
    else:
        raise ValueError('netto musi byc int lub float!')
        
    
print('cena_netto =',wyznaćCenuBrutto(15.6))
print('cena_netto =',wyznaćCenuBrutto(15))
print('cena_netto =',wyznaćCenuBrutto(-7))
print('cena_netto =',wyznaćCenuBrutto("9.20"))