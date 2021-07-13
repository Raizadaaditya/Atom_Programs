'''
Concate Program numpy

concatenating two numpy arrays
'''
import numpy as np

n = int(input("Enter rows for first array:"))
m = int(input("Enter rows for second array:"))
p = int(input("Enter cols for both arrays:"))

L1 = []
L2 = []
for i in range(n):
    a = []
    for j in range(p):
        num = int(input("Enter number for 1st list:"))
        a.append(num)
    L1.append(a)

for i in range(m):
    a = []
    for j in range(p):
        num = int(input("Enter number for 2st list"))
        a.append(num)
    L2.append(a)

arr1 = np.array(L1)
arr2 = np.array(L2)
print(np.concatenate((arr1,arr2)))
