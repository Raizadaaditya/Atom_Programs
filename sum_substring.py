'''
print the continuous sub strings that have required sum
'''
arr = []
n = int(input('Enter the number of elements you want '))
s = int(input('Enter the required sum '))

for i in range(n):
    ele = int(input('Enter Integer input '))

    arr.append(ele)
print(arr)

for j in range(n-1):
    if arr[j] + arr[j+1] == s:
        print(arr[j],arr[j+1])
    else:
        continue
