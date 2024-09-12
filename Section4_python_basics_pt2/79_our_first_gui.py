picture = [
    [0,0,0,1,0,0,0,],
    [0,0,1,1,1,0,0,],
    [0,1,1,1,1,1,0,],
    [1,1,1,1,1,1,1,],
    [0,0,0,1,0,0,0,],
    [0,0,0,1,0,0,0,],
]

counter = 0
while counter < 5:
    for row in picture:
        line = ''
        for item in row:
            line += ' ' if item == 0 else '*'
        print(line)
    print('*******************')
    print('*******************')
    print('*******************')
    counter += 1

