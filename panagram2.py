'''
finding missing Characters from the input
'''
gvn_str = "abcdefghijklmnopqrstuvwxyz "
inpt_str = "Online test with GS client "
lwr_str = inpt_str.lower()
count = []

for ch in gvn_str:
    if ch in lwr_str:
        continue
    else:
        count.append(ch)

print('Characters missing', count)
print('Number of Characters missing', len(count))
