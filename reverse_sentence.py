sentence = "I like coding in python"
reversed_sent = ""
for ch in range(len(sentence)-1, -1, -1):
    reversed_sent += sentence[ch]
    print(ch)
print(reversed_sent)
