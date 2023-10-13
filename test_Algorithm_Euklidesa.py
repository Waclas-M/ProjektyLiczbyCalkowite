#Silnia 4!= 1 * 2 * 3 * 4
def silnia(n):
    if n <= 0:
        return 1
    else:
        return n*silnia(n-1)

print(silnia(4))

def fibon(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibon(n-1) + fibon(n-2)

print(fibon(4))
