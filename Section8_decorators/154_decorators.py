def hello():
    print('Hellooooooo')

greet = hello

del hello

print(greet()) #does not delete the functionality, despite the deletion of the method hello

def hello2(func):
    return func()

def greet2():
    print('Called from another function!')

hello2(greet2)
#decorators work because of how python treats functions (first class citizens) e.g. they can also be used as variables