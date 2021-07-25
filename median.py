'''
sort two list as one list and find meadian of it
'''

lst1 = [2, 3, 6, 7, 9]
lst2 = [-1, 4, 8, 10]

final_lst = lst1 + lst2
fnl_sort_lst = final_lst.sorted()
print(fnl_sort_lst)


if (len(fnl_sort_lst)/2) == 0:
    median = fnl_sort_lst[(len(fnl_sort_lst)/2) + ((len(fnl_sort_lst)/2)+1)]
else:
    median = fnl_sort_lst[(len(fnl_sort_lst)+1)/2]

print(median)
