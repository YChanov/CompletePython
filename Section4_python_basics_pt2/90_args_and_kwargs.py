# *args  is to accept any number of arguments and work with them in the function
# *kwargs is to accept arguments, that are provided with key:value pairs as arguments to the function
# 'args' and 'kwargs' is a name convention, not mandatory naming
def super_func(*args):
    return sum(args)

print(super_func(1,2,3,4,5))

def super_func_kwargs(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total

print(super_func_kwargs(1,2,3,4,5, num1 = 10, num2 = 10))
