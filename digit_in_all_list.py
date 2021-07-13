'''
digit that repeated in all 3 list entered
'''
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
arr = []

for ch in arr1:
    if ch in arr2 and ch in arr3:
        arr.append(ch)
    else:
        continue
print(arr)
