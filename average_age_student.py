'''
finding average age of student in th list
[["Ramesh",30],["Suresh",49],["Ramesh",25],["Arjun",20]]
'''
lst = [["Ramesh", 30], ["Suresh", 49], ["Ramesh", 25], ["Arjun", 20]]
out_dict = {}
tot = 0
count = 0
for i in range(len(lst)):
    if lst[i][0] in out_dict:
        tot = tot + lst[i][1]
        count = count + 1
        out_dict[lst[i][0]] = tot/count
    else:
        out_dict[lst[i][0]] = lst[i][1]

print(out_dict)
