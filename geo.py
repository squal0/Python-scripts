##def geometric(lst):
##    for i in range(len(lst) - 1):
##        if lst[i] * lst[i + 1] != lst[i + 1] ** 1:
##            return False
##    return True

	

def check_arith(lst):

    l1 = len(lst) - 1
    n= 2

    dif = lst[1] - lst[0]

    while(n<l1):

        if (lst[n+1] - lst[n]) != dif: 
            return False
        else:
            n = n + 1
    return True
