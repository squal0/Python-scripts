def is_prime(x):
    """Function to determine whether x is a prime number """
    x = abs(x) #ensures that x is an absolute number
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range (2, x):
        if x % n == 0:
            return False
    return True
