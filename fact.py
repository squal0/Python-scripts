def recursive_factorial(n):
    if(n == 0):
        return 1
    else:
        return (n * recursive_factorial(n-1))

def iterative_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
