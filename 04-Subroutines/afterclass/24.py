def retMonthName(number):
    MonthNames = ['Styczeń',
                  'Luty',
                  'Marzec',
                  'Kwiecień',
                  'Maj',
                  'Czerwiec',
                  'Lipiec',
                  'Sierpień',
                  'Wrzesień',
                  'Październik',
                  'Listopad',
                  'Grudzień']
    if number > 0 and number < 13:
        return(MonthNames[number-1])
    else:
        return "Error"

print(retMonthName(1))