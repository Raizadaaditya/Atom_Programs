'''
check the occurance if each char in string
'''
inpt_str = input('Enter string ')
out_dict = {}

for ch in inpt_str:
    if ch in out_dict:
        out_dict[ch] += 1
    else:
        out_dict[ch] = 1
print(out_dict)
