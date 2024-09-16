while True:
    try:
        age = int(input('What is your age'))
        10/age # just for the sake of the example to toggle error if the user adds 0 as age
        print(age)
    except ValueError:
        print('please add a valid number')
        continue
    except ZeroDivisionError:
        print('age can not be zero')
        break
    else:
        break
    finally:
        print('OK I am finally done')
    print('can you hear me?')

#when there are breaks in a loop, nothing gets printed after the usual try-except-finally blocks
