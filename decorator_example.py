'''
Decorators + Closure
These are the functions with function as parameter
They use inner function which can be called as well as returned
and when they are returned they are
'''

def printer():
    print('Hello World!')

# passing function printer to display info function
def display_info(func, msg):

    def inner():
        print("Executing {} function".format(func.__name__))
        func()
        print("Inner function remembers the Message this is called closure")
        print("Message is: ", msg)
        print("Finished Execution")

    return inner

decorated_func = display_info(printer, 'Closure Message')
# calling decorated function
decorated_func()
