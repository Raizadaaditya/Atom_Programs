'''
finds the max average marks of a student
'''

inpt_lst = [  ["Rohit", "85"], ["Rahul", "80"], ["Amit","85"],["Rohit", "90"]  ]
opt_dict = dict()
opt_dict_avg = dict()
avg_lst = []


for i in range(len(inpt_lst)):
    if inpt_lst[i][0] not in opt_dict:
        opt_dict[inpt_lst[i][0]] = int(inpt_lst[i][1])
        opt_dict_avg[inpt_lst[i][0]] = 1
    else:
        opt_dict[inpt_lst[i][0]] += int(inpt_lst[i][1])
        opt_dict_avg[inpt_lst[i][0]] += opt_dict_avg[inpt_lst[i][0]]
print(opt_dict)
print(opt_dict_avg)


for (k1,v1), (k2,v2) in zip(opt_dict.items(),opt_dict_avg.items()):
    avg = v1/v2
    print(k1)
    print(avg)
    avg_lst.append(avg)
print('Max average value', max(avg_lst))
