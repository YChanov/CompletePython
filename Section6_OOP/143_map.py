# map accepts as first parameter function which is operating with the items in a given iterable
# the result is map object that can be cast also as list

def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, ([2, 3, 4]))))
