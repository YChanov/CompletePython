# filter is used to filter some of the items in an iterable by provided function for filtering

def odd(item):
    return item % 2 != 0

print(list(filter(odd, [1,2,34,5,6,6])))