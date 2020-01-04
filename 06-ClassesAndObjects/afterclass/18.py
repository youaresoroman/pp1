from random import randint

class Cube():
    def __init__(self):
        pass
    def throw(self):
        return randint(1,6)

def throwFun():
    throwCollector = []
    for i in range(1,4):
        c = Cube()
        throwCollector.append(c.throw())
        print(f'Rzut {i}: {c.throw()}')
    return f'Suma: {sum(throwCollector)}'
        
print(throwFun())