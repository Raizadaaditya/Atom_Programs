'''
l=[1,2,3,4,1,2,2,3,1,4]
out = {1:[0,4,8], 2:[1,5,6], 3:[2,7], 4:[3,9]}
using enumerator to find index of the items in list
'''

inpt_list = [1,2,3,4,1,2,2,3,1,4]
out = {}
enum_obj_list = list(enumerate(inpt_list))

for num in enum_obj_list:
    if num[1] in out:
        out[num[1]].append(num[0]) 
    else:
        temp_lst = [num[0]]
        out[num[1]] = temp_lst

print(out)