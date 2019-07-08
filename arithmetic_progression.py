def arithmetic_progression():
    '''Program asks for input from the user then calculates and prints out
    both the arithmetic progression sequence and the total of the numbers in
    in the sequence'''
    i = 1
    total = 0 #variable to store total
    terms = int(raw_input("Enter the number of terms: "))
    difference = int(raw_input("Enter the common difference of the AP: "))

    while ( i <= terms):
        ap = 1 + ( i - 1) * difference #code that the gets the arithmetic progression
        print ap
        total += ap
        i += 1

    return total
