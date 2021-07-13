'''
check if input tring is Panagram
'''
gvn_str = "abcdefghijklmnopqrstuvwxyz "
inpt_str = "The quick brown fox jumps over the lazy dog"
lwr_str = inpt_str.lower()
pan = 0

for ch in gvn_str:
    if ch in lwr_str:
        continue
    else:
        pan = 1
        break
if pan == 1:
    print('Not Panagram')
else:
    print('Panagram')
