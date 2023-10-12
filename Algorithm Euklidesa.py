def Eulkides(number,divider):
    solution = []
    if number < divider:
        x = number
        number = divider
        divider = x


    while number >1:
        ratio = number // divider
        rest = number - (ratio * divider)
        number = divider
        solution.append(rest)
        divider = rest
        if rest == 0:
            break

    return solution.pop(len(solution)-2)





print(aa(240,150))
