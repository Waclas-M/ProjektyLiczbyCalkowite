def distribution(n):
    solution=[]
    i = 2
    while n>1:
        while n % i == 0:
            solution.append(i)
            n = n/i
        i += 1
    return solution


