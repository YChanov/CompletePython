while True:
    try:
        age = int(input('What is your age'))
        10/age # just for the sake of the example to toggle error if the user adds 0 as age
        print(age)
    except ValueError:
        print('please add a valid number')
    except ZeroDivisionError:
        print('age can not be zero')
    else:
        break