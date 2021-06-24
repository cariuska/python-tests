def calc(type, a, b):
    if type == "+":
        return a + b
    elif type == "-":
        c = a - b
        if c < 0:
            return "Value Invalid"
        else:
            return c
    else:
        return "Error"
