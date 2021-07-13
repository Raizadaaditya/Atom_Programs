'''
print element with are occurred only once
'''
import numpy as np
arr = np.array([-1, -2, 3, 3, -2])
out_dict = {}
for num in arr:
    if num in out_dict:
        out_dict[num] += 1
    else:
        out_dict[num] = 1
for key,val in out_dict.items():
    if val != 1:
        continue
    else:
        print(key)
