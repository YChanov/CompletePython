#find duplicates in the list

some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']
uniques_list = []

for item in some_list:
    if item in uniques_list:
        print(item)
    else:
        uniques_list.append(item)
