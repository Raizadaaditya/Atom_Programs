'''
Symmetric difference - Set
'''

set1 = set()
set2 = set()

M = int(input("Length of Set1: "))

for i in range(M):
    inpt = int(input('Enter number in set1: '))
    set1.add(inpt)

N = int(input("Length of Set2: "))

for i in range(N):
    inpt = int(input('Enter number in set2: '))
    set2.add(inpt)

sem_diff = set1.symmetric_difference(set2)
# only numbers which are unique to both sets will be there in sem_diff

print("Symmetric difference: ")
for num in sem_diff:
    print(num)
