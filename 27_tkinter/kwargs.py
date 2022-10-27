def calculate(n, **kwargs):         # kwargs get passed as dictionary
    print(kwargs)
    # for key, value in kwargs.items():
    # print(key)
    # print(value)
    n += kwargs['add']
    print(n)
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')      # get eases by giving none
        self.model = kw.get('model')


my_car = Car(make='Nissan')
print(my_car.model)
