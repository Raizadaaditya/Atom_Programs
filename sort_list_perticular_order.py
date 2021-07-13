'''
sort the list in given order only
'''
inpt_lst = ["Ajay", "Raja", "Keshav", "List", "Set", "Elephant", "Drone"]
sort_ord = 'TESARDLK'
out_lst = []

for ch in sort_ord:
    for name in inpt_lst:
        if ch != name[0]:
            continue
        else:
            out_lst.append(name)
print(out_lst)
