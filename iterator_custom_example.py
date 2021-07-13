'''
Custom Iterators
using class printing even numbers to a maximum range
'''

class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max

    #def __iter__(self):
        #return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration

numbers = Even(10)
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
# or
#print(next(numbers))
#print(next(numbers))
#print(next(numbers))
