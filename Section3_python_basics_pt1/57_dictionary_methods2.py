from cgi import print_exception

user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

print('basket' in user)
print('greet' in user.keys())
print('hello' in user.values())
print(user.items())

# user.clear()
# print(user)

user2 = user.copy()
print(user2)

popped_item = user.popitem()

print(popped_item)
print(user)

user.update({'greet': 'yeahh'})
print(user)

user.update({'new_key': 'killer dog'})
print(user)