'''

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])

'''

A = set()

n = int(input('Enter Length of set A: '))

for i in range(n):
    inpt = int(input('Enter number in Set A: '))
    A.add(inpt)

print(A)
N = int(input('Enter number of operations: '))

for op in range(N):
    S = set()
    oper = input('Enter name of operation {}: '.format(op+1))
    m = int(input('Enter Length of Set S: '))

    for i in range(m):
        inpt = int(input('Enter number in Set S: '))
        S.add(inpt)

    if oper == 'update':
        A.update(S)
        print('A:')
        print(A)
    elif oper == 'intersection_update':
        A.intersection_update(S)
        print('A:')
        print(A)
    elif oper == 'difference_update':
        A.difference_update(S)
        print('A:')
        print(A)
    elif oper == 'symmetric_difference_update':
        A.symmetric_difference_update(S)
        print('A:')
        print(A)
