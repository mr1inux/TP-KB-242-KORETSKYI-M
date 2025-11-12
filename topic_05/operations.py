
def dia():
    w = input("Dia: ")
    if w == "ex":
        return 'exit'
    else:
        return w


def num(nomer):
    while True:
        try:
            num = (input(f"{nomer} num: "))
            n = float(num)
            return n
        except ValueError:
            print(f"'{num}': is not integer")
