'''
Survivor list program
Removing the elements from the list and increasing the steps at every interation
'''

main_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_list = []

step = 2
main_len = len(main_list)
while(step < main_len):
    for n in range(0, main_len, step):
        new_list.append(main_list[n])
    main_list = new_list
    main_len = len(main_list)
    new_list = []
    step = step + 1

print(main_list)