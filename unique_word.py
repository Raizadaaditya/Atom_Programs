'''
Print unqiue words in the string
'''
inpt_str = 'Good day bye bye'
inpt_lst = list(inpt_str.split(' '))
out_list = []
for wrd in inpt_lst:
    if wrd not in out_list:
        out_list.append(wrd)
    else:
        continue

out_str = ' '.join(out_list)
print(out_str)
