'''
find weight of String
'''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str1 = input("Enter String for weight ").lower()
total = 0

for ch in str1:
    if ch in alphabet:
        total = total + (alphabet.index(ch)+1)

print(total)
