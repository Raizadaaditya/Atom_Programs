'''
Exception Handling using try catch and finally block
'''

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

    print(result)

    my_list = [1, 2, 3]
    i = int(input("Enter index: "))
    print(my_list[i])
except ZeroDivisionError:
    print("Denominator cannot be 0. Try again.")
except IndexError:
    print("Index is wrong.")

finally:
    print("Program ends")
