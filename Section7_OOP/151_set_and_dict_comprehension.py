# set comprehension works the same as the list

my_set2 = {num for num in range(0, 100)}
print(my_set2)

my_set3 = {num ** 2 for num in range(0, 100)}
print(my_set3)

# dictionaries
simple_dict = {
    'a': 3,
    'b': 4
}

my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}

print(my_dict)

my_dict = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)
