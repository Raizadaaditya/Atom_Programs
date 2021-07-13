'''
Finding missing numbers from user input set of numbers
total numbers = 5
entered numbers = 1 2 4 5
missing number = 4
'''
tot = int(input("Enter total number of values set should have: "))
inpt_str = input("Enter space sperated values: ")
out_lst = []

# converting input values to list
inpt_lst = inpt_str.split(' ')

# convering input list values to integer type
for i in range(len(inpt_lst)):
    inpt_lst[i] = int(inpt_lst[i])

# adding the numbers which doesn't exist in input to output list
for i in range(tot):
    if (i+1) not in inpt_lst:
        out_lst.append(i+1)

# print list of missing values
print(out_lst)
