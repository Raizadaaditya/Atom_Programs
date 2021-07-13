'''
Find method in string
to check if substring entered by user exist in main text
'''

txt = 'BootcampxobinaoKgo'
sub = 'xobin'

res = txt.find(sub)
print(res)                  # printing index number at which substring started

if res > 0:
    print("Sub exist")
else:
    print("Doesn't exist")
