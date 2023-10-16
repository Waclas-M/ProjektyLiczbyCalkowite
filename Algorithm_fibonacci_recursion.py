def fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2 )

