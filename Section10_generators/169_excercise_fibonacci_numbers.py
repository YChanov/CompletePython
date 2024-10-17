# f0 f1 f2 f3 f4 f5 f6
# 0  1  1  2  3  5  8

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(21):
    print(x)


def fib_list(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b