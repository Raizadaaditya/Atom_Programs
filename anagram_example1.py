'''
l1: ['eat', 'ate', 'tea', 'ant', 'tan', 'bat']
l2: [['eat', 'ate', 'tea'],['ant, tan'], ['bat']]

generic program even the order of l1 is changed
still it will find the anagrams
'''

inpt_lst = ['eat', 'ate', 'ant', 'tea', 'tan', 'bat']
out_dict = {}

for wrd in inpt_lst:

    sorted_wrd = sorted(wrd)
    sorted_wrd = ''.join(sorted_wrd)
    if sorted_wrd in out_dict:
        out_dict[sorted_wrd].append(wrd)
    else:
        out_dict[sorted_wrd] = []
        out_dict[sorted_wrd].append(wrd)

out_lst = out_dict.values()
print(out_lst)
