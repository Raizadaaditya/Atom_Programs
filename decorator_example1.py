'''
decorators using @ symbol
'''

# passing function printer to display info function


def display_info(func):

    def inner():
        print("Executing {} function".format(func.__name__))
        func()
        print("Finished Execution")

    return inner


@display_info
def printer():
    print('Hello World!')


printer()
