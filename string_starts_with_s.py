'''
check if string starts with S
'''
inpt_lst = ["apple","sample", "search","cat"]
out_lst = []

for word in inpt_lst:
    if word[0] == 's' or word[0] == 'S':
        out_lst.append(word)
print(out_lst)
