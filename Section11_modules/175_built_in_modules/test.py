import random

print(random.random())
print(random.randint(1, 10))
print(random.choice([1,2,3,4,5]))

my_list = [1,2,3,4]
random.shuffle(my_list)
print(my_list)