'''
first non repeating char
'''

inpt_lst= [ "array", "apple", "rat", "aabbcdde"]
wrd_dict = dict()

for wrd in inpt_lst:
    for ch in wrd:
        if ch in wrd_dict:
            wrd_dict[ch] = wrd_dict[ch] + 1
        else:
            wrd_dict[ch] = 1
    for key,val in wrd_dict.items():
        if val !=1:
            continue
        else:
            print('key:{} value:{}'.format(key,val))
            wrd_dict = dict()
            break
