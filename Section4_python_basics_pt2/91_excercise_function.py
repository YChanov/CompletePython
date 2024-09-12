def highest_even(list_of_numbers=[]):
    highest_even_number = 0
    for item in list_of_numbers:
        if item % 2 == 0:
            highest_even_number = item if item > highest_even_number else highest_even_number
    return highest_even_number


print(highest_even([1, 2, 3, 4, 5, 10, 122]))
