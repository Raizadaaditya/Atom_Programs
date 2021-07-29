'''
Merging two list into dictionary
'''

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

out_dict = {}

for ch, n in zip(l2, l1):
    out_dict[ch] = n

print(out_dict)
