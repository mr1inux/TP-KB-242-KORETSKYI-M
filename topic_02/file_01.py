import math

a = float(input("A num: "))
b = float(input("B num: "))
c = float(input("C num: "))


def ds(a, b, c):
    n = b**2-4*a*c
    return n


def q(a, b, c):
    d = ds(a, b, c)
    print('d='+str(d))

    if d > 0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print('x1='+str(x1)+'; x2='+str(x2))
    elif d == 0:
        x = (-b/(2*a))
        print('x='+str(x))
    else:
        print('Error!')


q(a, b, c)
