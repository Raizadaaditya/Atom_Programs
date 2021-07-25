'''
Print perfect number between a range
For example: 6 is the first perfect number
Proper divisors of 6 are 1, 2, 3
Sum of its proper divisors = 1 + 2 + 3 = 6.
Hence 6 is a perfect number.
'''
start = int(input('Enter start num '))
end = int(input('Enter end num '))

for i in range(start, end + 1):
    sum1 = 0
    for x in range(1, i):
        if(i % x == 0):
            sum1 += x
            if (sum1 == i):
                print(i)
