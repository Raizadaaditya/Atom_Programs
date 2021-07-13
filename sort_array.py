'''
merge two arrays and sort the final one
'''
import numpy as np
arr1 = np.array([1,3,4,5])
arr2 = np.array([2,4,6,8])

arr3 = np.concatenate((arr1,arr2))
print(np.sort(arr3))
