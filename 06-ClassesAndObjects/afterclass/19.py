class account():
    def __init__(self,number):
        self.number = number
        self.saldo = 0
    def __str__(self):
        return f'Number: {self.number}\nSaldo: {self.saldo} ' 
    def cash_in(self,cashIn):
        self.saldo += cashIn
        return self.saldo
    def cash_out(self,cashOut):
        self.saldo -= cashOut
        return self.saldo
    
acc = account('12 3456 5555 9090 1111 0000 7722')
print(acc)
acc.cash_in(25.30)
print(acc)
acc.cash_in(31.70)
print(acc)
acc.cash_out(14)
print(acc)