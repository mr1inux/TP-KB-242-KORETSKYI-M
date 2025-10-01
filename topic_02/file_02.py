W = input("Dia: ")
a = float(input("F num: "))
b = float(input("S num: "))

if W == "+":
    c = a+b
    print('Result: '+str(c))

elif W == "-":
    c = a-b
    print('Result: '+str(c))

elif W == "*":
    c = a*b
    print('Result: '+str(c))

elif W == "/":
    c = a*b
    print('Result: '+str(c))
else:
    print('Error!')
