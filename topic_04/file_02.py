while True:
    try:
        print('--------------------------------')
        W = input("Dia: ")
        if W == "ex":
            print('exit')
            break
        a = int(input("F num: "))

        b = int(input("S num: "))

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
    except Exception as wr:
        print(wr)
