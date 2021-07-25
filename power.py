'''
check if x is power of y
'''
x = int(input('Enter x: '))
y = int(input('Enter y: '))

pow = 1
i = 0
if x > 0 and y > 0:
    if x == 1 and y != 1:
        print("{} power 0 is {}".format(y, x))
    elif x == y:
        print("{} power 1 is {}".format(y, x))
    else:
        while (pow < x):
            pow = pow * y
            i += 1
        if pow == x:
            print("{} power {} is {}".format(y, i, x))
        else:
            print("{} doesn't come with any power of {}".format(x, y))
else:
    print('not valid input')
