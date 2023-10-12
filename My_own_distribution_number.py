def a(liczba):
    list = []
    x = 2
    while liczba > 1:
        if liczba % x == 0:
            list.append(x)
            liczba = liczba / x
            x -= 1
        else:
            pass
        x += 1

    return list


