'''
finding mininum and maximum values of list
'''

lst = [4, 5, 1, 2, 9]

min = max = lst[0]
for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]
    if lst[i] > max:
        max = lst[i]

print(min)
print(max)
