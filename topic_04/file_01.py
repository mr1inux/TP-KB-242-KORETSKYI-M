
while True:
    try:
        print('--------------------------------')
        W = input("Dia: ")
        if W == "ex":
            print('exit')
            break
        num = (input("F num: "))
        a = int(num)
        num = (input("S num: "))
        b = int(num)

        match W:
            case "+":
                c = a + b
                print('Result: ' + str(c))
            case "-":
                c = a - b
                print('Result: ' + str(c))
            case "*":
                c = a * b
                print('Result: ' + str(c))
            case "/":
                try:
                    c = a / b
                    print('Result: ' + str(c))
                except ZeroDivisionError:
                    print("ZeroDivisionError")
            case _:
                print('Error!')
    except ValueError:
        print(f"{num}: is not integer")
