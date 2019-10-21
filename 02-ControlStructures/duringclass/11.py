dbuser = 'marek'
dbpwd = 'wx15'

inputuser = str(input("Podaj login: "))
inputpwd = str(input("Podaj hasło: "))

if dbuser == inputuser and inputpwd == dbpwd:
    print("Podane dane są prawidłowe")
else:
    print("Podane dane są nieprawidłowe")