'''
Shallow and Deep copy
'''
import copy


'''
two variables/list shares same Address having different value names
using '=' operator for this
'''
list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = list1
print('List1: ', list1)
print('Address of list1: ', id(list1) )
print('list2: ', list2)
print('Address of list2: ', id(list2) )
print('')
list1.append([10,11,12]) #adding new element to old list
print('List1: ', list1)
print('List2: ', list2)

'''
Shallow copy other variable/list copies the reference
using copy method from Copy module
It copies the reference of the objects doesn't creates copies of the objects
'''
old_list_shallow = [[1,2,3],[4,5,6],[7,8,9]]
new_list_shallow = copy.copy(old_list_shallow)

print('')
print('Old list shallow: ', old_list_shallow)
print('Address of old_list_shallow:', id(old_list_shallow))
print('New list shallow: ', new_list_shallow)
print('Address of new_list_shallow:', id(new_list_shallow))

#adding new element to old list would not be reflected in new list
print('')
old_list_shallow.append([4,4,4])
print('Old list shallow: ', old_list_shallow)
print('New list shallow: ', new_list_shallow)

#updating element in old list will be reflected in new one too
print('')
old_list_shallow[1][1] = 'AA'
print('Old list shallow: ', old_list_shallow)
print('New list shallow: ', new_list_shallow)

'''
Deep copy using deepcopy method from Copy module
using deep copy it copies the value in the new list means seperate copy is created
'''
old_list_deep = [[1,2,3],[4,5,6],[7,8,9]]
new_list_deep = copy.deepcopy(old_list_deep)

print('')
print('Old list deep: ', old_list_deep)
print('Address of old_list_deep:', id(old_list_deep))
print('New list deep: ', new_list_deep)
print('Address of new_list_deep:', id(new_list_deep))

#adding new element to old list would not be reflected in new list
print('')
old_list_deep.append([3,3,3])
print('Old list deep: ', old_list_deep)
print('New list deep: ', new_list_deep)

#updating element in old list will not be reflected in new list
print('')
old_list_deep[1][1] = 'BB'
print('Old list deep: ', old_list_deep)
print('New list deep: ', new_list_deep)
