#pristupamo promenljivima u funkciji po poziciji
def add(*args):
    print(args[1])
    sum = []
    for n in args:
        sum.append(n)
    return sum

print(add(['a','c'],['d','s'],[1,2],'ale','o',('groabare','da','karamo')))
print('----------------------------------------------')
#pristupamo promenljivima u funkciji po imenima

def calculate(n,**kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    #
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3,multiply=5)

# pravimo klasu sa key words

class MyCar:

    def __init__(self,**kw):
        # koristimo get metod jer prilikom pozivanja klase, objekat ce biti izgradjen sa difolt vrednostima None
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')

car = MyCar(make='BMW',color='red')
print(car.make,car.model,car.color)