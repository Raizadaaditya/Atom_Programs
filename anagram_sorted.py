'''
anagram using sorted function only
'''

def check_anagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("Strings are anagram")
    else:
        print("Strings aren't anagram")

str1 = input("Enter first string ")
str2 = input("Enter Second string ")

check_anagram(str1,str2)
