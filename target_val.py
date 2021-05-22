'''
Finding number reaching the target value user gave
user list = [1,5,6,8,9,3]
target value = 15
o/p = [6,9] makes total 15
'''
inpt_dict = {}
out_lst = []
# talking input of numbers in space seperated string values
inpt_str = input("Enter space sperated values: ")
target = int(input("Enter target value: "))
# converting string into list
inpt_lst = inpt_str.split(' ')
# convering each element to integer type
for i in range(len(inpt_lst)):
    inpt_lst[i] = int(inpt_lst[i])

# assigning by default value of each input as False
for ch in inpt_lst:
    if ch not in inpt_dict:
        inpt_dict[ch] = False

# checking if any other values exist which is equal to difference
# of input value and target value
# assigning the value to True
for ch in inpt_dict:
    if (target - ch) in inpt_dict:
        inpt_dict[ch] = True

# checking if value in dictionary exist with True
# if Yes then appending those values to output list
for k,v in inpt_dict.items():
    if v == True:
        out_lst.append(k)

# printing the list of values that makes target value
print(out_lst)
