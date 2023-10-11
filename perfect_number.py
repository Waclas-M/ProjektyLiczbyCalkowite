#liczba doskonola to taka liczba ktorej dzielniki po dodaniu sa rowne liczbie

def perfect(number):
    list_of_divider = []
    result = 0
    for x in range(1,number+1):
        divider  = number % x
        if divider == 0:
            list_of_divider.append(x)
        else:
            pass
    for i in list_of_divider:
        result += i
    solution = result - number
    if solution == number:
        return 'Liczba doskonala'
    else:
        return 'Nie liczba doskonala'


