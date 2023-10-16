def NWD(a, b):
    if b != 0:
        return NWD(b, a % b)
    return a

