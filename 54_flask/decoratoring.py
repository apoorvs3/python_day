import time

"""decorator function is a function which wraps another function and gives it some additional functionality or 
modifies the functionality"""


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print('hello')


@delay_decorator
def say_bye():
    print('bye')


def say_greet():
    print('how are you')



# one way to call
say_hello()

# other way
delay_dec = delay_decorator(say_greet)
delay_dec()
