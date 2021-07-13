'''
check if 1st and 2nd string are anagram or not
'''
str1 = input("Enter first string ")
str2 = input("Enter Second string ")

str1_dict = {}
str2_dict = {}

if len(str1) == len(str2):
    for ch in str1:
        if ch in str1_dict:
            str1_dict[ch] += 1
        else:
            str1_dict[ch] = 1
    for ch in str2:
        if ch in str2_dict:
            str2_dict[ch] += 1
        else:
            str2_dict[ch] = 1

    if str1_dict == str2_dict:
        print('Anagram')
    else:
        print('Not Anagram')
