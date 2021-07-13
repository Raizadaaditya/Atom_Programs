'''
remove common characters from the given string
'''
inpt = 'aditya'
out_lst = []

for ch in inpt:
    if ch in out_lst:
        continue
    else:
        out_lst.append(ch)
out_str = ''.join(out_lst)
print(out_str)
