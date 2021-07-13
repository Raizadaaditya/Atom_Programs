'''
Numerology of name etered
'''
total = 0
str1 = 'S. KANAPATHY'

for ch in str1:
    if ch in {'A','I','J','Q','Y'}:
        total += 1
    elif ch in {'B','K','R'}:
        total += 2
    elif ch in {'C','G','L','S'}:
        total += 3
    elif ch in {'D','M','T'}:
        total += 4
    elif ch in {'E','H','N','X'}:
        total += 5
    elif ch in {'U','V','W'}:
        total += 6
    elif ch in {'O','Z'}:
        total += 7
    elif ch in {'F','P'}:
        total += 8
    else:
        continue

new_total = total
num = 0
while new_total > 0:
    n = new_total % 10
    num += n
    new_total = new_total//10
print(num)
