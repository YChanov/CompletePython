# pure functions always return the same response with the same input
# pure functions don't have side effects

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([2, 3, 4]))
