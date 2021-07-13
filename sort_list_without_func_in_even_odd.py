'''
sorting list into odd descending
and even ascending numbers
i/p -> A = [1,2,3,5,4,7,10]
o/p -> A = [7,5,3,1,2,4,10]
wihout using sort function
'''

tot = int(input("Enter the length of list: ")) # total length of list
my_list_str = input("Enter the list of numbers seperated by space: ")
# splitting list values and making it into list

my_list = my_list_str.split(' ')
my_new_list = []

# checking if length entered and actual lengthare same
if tot == len(my_list):
    # converting list values into integer type
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    odd_lst = []
    new_odd_list = []
    even_lst = []
    new_even_list = []

    # checking if number is odd or even and putting into two different lists
    for num in my_list:
        if num%2 == 0:
            even_lst.append(num)
        else:
            odd_lst.append(num)

    # sorting odd list in descending order
    while odd_lst:
        max = odd_lst[0]
        for x in odd_lst:
            if x > max:
                max = x
        new_odd_list.append(max)
        odd_lst.remove(max)

    # sorting even list in ascending order
    while even_lst:
        min = even_lst[0]
        for x in even_lst:
            if x < min:
                min = x
        new_even_list.append(min)
        even_lst.remove(min)

    # conbining both sorted lists
    my_new_list = new_odd_list + new_even_list
    print(my_new_list)

else:
    print("Entered total number of items doesn't match with actually entered")
