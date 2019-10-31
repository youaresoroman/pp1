user = 'marek'
pwd = 'wx15'

inuser = str(input("Podaj login: "))
inpwd = str(input("Podaj hasło: "))

if user == inuser and  pwd == inpwd:
    print("Podane dane są prawidłowe")
else:
    print("Podane dane są nieprawidłowe")