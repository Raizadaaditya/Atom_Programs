def sum_of_digit(num):
    temp = num
    total = 0
    while temp > 0:
        rem = temp % 10
        total = total + rem
        temp = int(temp/10)
    if total > 9:
        return sum_of_digit(total)
    if total == 9:
        return True


inpt_num = [7089, 3000, 2403, 6090, 8181, 8001]
out_lst = []
for num in inpt_num:
    bol_res = sum_of_digit(num)
    if bol_res == True:
        out_lst.append(num)

print(out_lst)
