'''
Symmetric difference - Set
'''

set1 = set()
set2 = set()

M = int(input("Length of Set1: "))

for i in range(M):
    inpt = int(input())
    set1.add(inpt)

N = int(input("Length of Set2: "))

for i in range(N):
    inpt = int(input())
    set2.add(inpt)

set1_diff = set1.difference(set2)
set2_diff = set2.difference(set1)
sem_diff = set1_diff.union(set2_diff)

print("Symmetric difference: ")
for num in sem_diff:
    print(num)
