def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('Helloooo')


@my_decorator
def bye():
    print('See you later!')

bye()