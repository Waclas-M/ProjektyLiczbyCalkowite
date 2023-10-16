def Euklides(number,divider):
    solution = []

    while number >1:
        change = number % divider
        number = divider
        solution.append(change)
        divider = change
        if change == 0:
            break

    return solution.pop(len(solution)-2)


