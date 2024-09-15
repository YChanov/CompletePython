# do a list based on the characters in a string

my_list = []

for char in 'Hello':
    my_list.append(char)

print(my_list)

# doing it with comprehension
my_list = [char for char in 'Hello']
print(my_list)

# additional examples
my_list2 = [num for num in range(0, 100)]
print(my_list2)

my_list3 = [num ** 2 for num in range(0, 100)]
print(my_list3)

# keep only the even numbers
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
