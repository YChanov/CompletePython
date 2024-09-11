user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

# print(user['age']) #throws keyerror
print(user.get('age', 55))

user2 = dict(name = 'Jojo')