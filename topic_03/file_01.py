
while True:
    print('--------------------------------')
    W = input("Dia: ")
    if W == "ex":
        print('exit')
        break
    a = float(input("F num: "))
    b = float(input("S num: "))

    match W:
        case "+":
            c = a+b
            print('Result: '+str(c))
        case "-":
            c = a-b
            print('Result: '+str(c))
        case "*":
            c = a*b
            print('Result: '+str(c))
        case "/":
            c = a/b
            print('Result: '+str(c))
        case _:
            print('Error!')
