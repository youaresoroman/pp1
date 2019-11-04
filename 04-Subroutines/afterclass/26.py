def podatek(dochod):
    if dochod < 5000 or dochod == 5000:
        return int(dochod*0.17)
    if dochod > 5000:
        return int(5000*0.17+(dochod-5000)*0.32)
    
print("Podatek należny:", podatek(int(input("Podaj dochód: "))), end =" zł\n")