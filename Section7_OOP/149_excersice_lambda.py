# do lambda that squares the list of items
my_list = [5, 4, 3]
print(list(map(lambda item: item * item, my_list)))

# do lambda list sorting. Sort this list by the second value in the tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key = lambda tuple: tuple[1])
print(a)