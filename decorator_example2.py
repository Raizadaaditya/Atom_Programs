def f1(a,b):
    res=a/b
    print(res)

def check(f1,a,b):
    if b != 0:
        return f1(a,b)
    else:
        print("second value is Zero")


a = 5
b = 0
check(f1,a,b)