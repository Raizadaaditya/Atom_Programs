'''
swaping key and values between two dictionaries
inpt_dict = {'k1' : 1, 'k2' : 2, 'k3' : 3, 'k4' : 1, 'k5' : 2, 'k6' : 3}
out_dict = {1 : ['k1','k4'], 2 : ['k2','k5'], 3 : ['k3','k6']}
'''
inpt_dict = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 1, 'k5': 2, 'k6': 3}
out_dict = {}

for k, v in inpt_dict.items():

    if v in out_dict:
        out_dict[v].append(str(k))
    else:
        out_dict[v] = []
        out_dict[v].append(str(k))

print(out_dict)
