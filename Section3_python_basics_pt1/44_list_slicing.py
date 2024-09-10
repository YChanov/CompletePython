amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes',
]

print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
print(amazon_cart[0::3])

another_cart = amazon_cart[:]
another_cart[0] = 'byke'
print(another_cart)
