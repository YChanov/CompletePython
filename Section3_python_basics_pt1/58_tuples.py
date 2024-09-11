# Tuple
# tuples are immutable

my_tuple = (1, 2, 3, 4, 5)

print(5 in my_tuple)

# tuples can be used as keys in dict
user = {
    (1, 2): [1, 2, 3],
    'greet': 'Hello',
    'age': 35
}

print(user[(1, 2)])
