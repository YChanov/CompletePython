basket = [1,2,3,4,5,6]

#adding
basket.append(8)
print(basket)

basket.insert(3, 100)
print(basket)

new_list = basket.extend([100,101])
print(basket)

#removing
basket.pop()
print(basket)

basket.pop(0)
print(basket)

basket.remove(4)
print(basket)

basket.clear()
print(basket)