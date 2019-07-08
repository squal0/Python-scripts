def geometric_progression():
    '''Program to generate a geometric series and calculate it's total'''
    i = 0
    total = 0
    terms = int(raw_input("Enter the number of terms: "))
    first = int(raw_input("Enter the first term of the Geometric series: "))
    ratio = int(raw_input("Enter the common ratio: "))
    value  = first

    while ( i < terms ):
        value *= ratio
        print value
        total += value

        i += 1
    return total
        
