# sets is data structure with unique values
# there can't be duplicates as values
my_set = {1, 2, 3, 4, 5, 5}

print(my_set) #there is only one 5 in the values

my_set.add(100)
my_set.add(2) #this is duplicate and it won't be added
print(my_set)

my_list = [1,2,3,4,5,5]
set_from_my_list = set(my_list)

print(set_from_my_list)