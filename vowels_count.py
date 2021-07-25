fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print(fname, "is wrong file name")
    exit()
vowels = {'a': 0, 'A': 0, 'e': 0, 'E': 0, 'i': 0,
          'I': 0, 'o': 0, 'O': 0, 'u': 0, 'U': 0}

for ch in fh.read():
    if ch in vowels:
        vowels[ch] += 1
    else:
        continue
print(vowels)
