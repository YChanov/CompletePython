# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_abby = Cat('Abby',10)
cat_jasper = Cat('Jasper', 4)
cat_felix = Cat('Felix', 1)

# 2 Create a function that finds the oldest cat
def get_elderly_mammal(list_with_animals):
    highest_age = 0
    oldest_mammal = None
    for animal in list_with_animals:
        if animal.species != 'mammal':
            continue
        if animal.age and highest_age < animal.age:
            highest_age = animal.age
            oldest_mammal = animal
    return oldest_mammal

oldest_cat = get_elderly_mammal([cat_abby, cat_felix, cat_jasper])

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat.name} and it is {oldest_cat.age} years old')


###########################
# solution from the course:
###########################


# Exercise Cats Everywhere
# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')