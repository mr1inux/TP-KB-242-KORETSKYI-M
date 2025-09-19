a = float(input("A num: "))
b = float(input("B num: "))
c = float(input("C num: "))


def ds(a, b, c):
    n = b**2-4*a*c
    return n


d = ds(a, b, c)
print(d)
