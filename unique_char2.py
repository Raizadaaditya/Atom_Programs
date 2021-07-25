'''
check if string has unique characters or not
'''
inpt_str = 'aditya'
out_dict = {}
ans = True

for ch in inpt_str:
    if ch in out_dict:
        out_dict[ch] += 1
    else:
        out_dict[ch] = 1

for val in out_dict.values():
    if val == 1:
        continue
    else:
        ans = False  # means characters in string are not unique
        break
print(ans)
