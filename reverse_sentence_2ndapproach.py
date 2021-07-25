'''
reading string from backwards without change words
'''

name = "python is good competitor to JAVA"
lst = name.split()

for i in range(len(lst)-1, -1, -1):
    print(lst[i])
