def fun(w, a, b):
    match w:
        case "+":
            c = a+b
            return c
        case "-":
            c = a-b
            return c
        case "*":
            c = a*b
            return c
        case "/":
            try:
                c = a/b
                return c
            except ZeroDivisionError:
                return "ZeroDivisionError"

        case _:
            return 'Error!'
