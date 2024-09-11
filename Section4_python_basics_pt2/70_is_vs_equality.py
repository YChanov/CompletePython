print(True == 1) #true
print('' == 1) #false
print([] == 1) #false
print(10 == 10.0) #true
print([] == []) #true


print(True is 1) #false
print('' is 1) #false
print('1' is 1) #false
print('1' is '1') #true
print([] is 1) #false
print(10 is 10) #true
print([] is []) #false

# equality checks for truthy comparison
# but 'is' is checking if the compared values are with the same memory alocation


