'''
Numpy concate approach 2
'''
import numpy as np

# talking input in string, splitting and converting
# string to integer
n,m,p = map(int,input().split())

# both list that would be converted to numpy array
L1 = []
L2 = []
for i in range(n):
    a = []
    a = list(int(j) for j in input().split()) # talking input from user and appending input into list
    L1.append(a) # appending list a to L1 list

# similar approach with list L2 like list L1 above
for i in range(m):
    a = []
    a = list(int(j) for j in input().split())
    L2.append(a)

arr1 = np.array(L1)
arr2 = np.array(L2)
print(np.concatenate((arr1,arr2)))
