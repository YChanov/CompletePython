some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']
uniques_list = []

for item in some_list:
    if some_list.count(item) > 1:
        if item not in uniques_list:
            uniques_list.append(item)

print(uniques_list)

#do the same with comprehension
uniques_list = list(set([item for item in some_list if some_list.count(item) > 1]))
print(uniques_list)