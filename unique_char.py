'''
unique characters of the string
'''
inpt_str = input('Enter string ')
out_list = []
for ch in inpt_str:
    if ch not in out_list:
        out_list.append(ch)
    else:
        continue
print(out_list)
