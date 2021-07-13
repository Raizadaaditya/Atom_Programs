'''
moving cursor in grid
'''

pos = [0,0]

str1 = 'RRULDDDLR'

for ch in str1:
    if ch == 'L':
        pos[0] = pos[0] - 1
    elif ch == 'R':
        pos[0] = pos[0] + 1
    elif ch == 'U':
        pos[1] = pos[1] + 1
    elif ch == 'D':
        pos[1] = pos[1] - 1
    else:
        print('Not recognissed command')
        break
print(pos)
