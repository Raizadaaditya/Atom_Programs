'''
swap case of string without using inbuilt function
Ascii code A-Z = 0065 - 0090
           a-z = 0097 - 0122
'''


def swap_case(str_data):
    result = ''
    caps = range(65, 91)
    small = range(97, 123)
    for char in str_data:
        if ord(char) in caps:
            result += chr(ord(char) + 32)

        elif ord(char) in small:
            result += chr(ord(char) - 32)

        else:
            print('{} Not an alphabet'.format(char))
            break
    return result


print(swap_case('AbDecFg'))
