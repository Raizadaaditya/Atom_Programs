'''
Generator example
it uses Yield keyword to generate next object
'''

def even_generator(max):
    n = 2
    while n <= max:
        yield n
        n += 2
num = even_generator(6)
print(next(num))
print(next(num))
print(next(num))
