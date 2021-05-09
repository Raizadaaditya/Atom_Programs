'''
seq = "aab" ; arr1={"dog", "dog", "cat"}   || output : true
seq = "aaa" ; arr2={"dog", "dog", "dog"}   || output : true
seq = "bba" ; arr2={"cat", "cat", "cat"}   || output : false
'''
seq = 'aab'
arr1 = ['dog', 'dog', 'cat']

for ch in seq:
    if ch[0] == ch[1]:
        if ch[0] == ch[2]:
            pass
        else:
            pass
    elif ch[1] == ch[2]:
        pass
