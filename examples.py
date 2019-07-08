##x = int(raw_input("Please enter a number: "))
##ans = 0
##if x >= 0:
##    while ans * ans < x:
##        ans += 1
##        print 'ans =', ans
##    if ans * ans != x:
##        print x, 'is not a perfect square'
##    else:
##        print ans
##else:
##    print x, 'is a negative number'

##def sqrt(x):
##    """Returns the square root of x, if x is a perfect square,
##        prints an error message and returns None otherwise"""
##    ans = 0
##    if x >= 0:
##        while ans * ans < x:
##            ans += 1
##        if ans * ans != x:
##            print x, 'is not a perfect square'
##            return None
##        else:
##            return ans
##    else:
##        print x, 'is a negative number'
##        return None

##def solve(numLegs, numHeads):
##    for numSpiders in range(0, numHeads + 1):
##        for numChicks in range(0, numHeads - numSpiders + 1):
##            numPigs = numHeads - numChicks - numSpiders
##            totLegs = 4 * numPigs + 2 * numChicks  + 8 * numSpiders
##            if totLegs == numLegs:
##                return(numPigs, numChicks, numSpiders)
##    return(None, None, None)
##
##def barnYard():
##    heads = int(raw_input('Enter the number of heads: '))
##    legs  = int(raw_input('Enter the number of legs: '))
##    pigs, chickens, spiders = solve(legs, heads)
##    if pigs == None:
##        print "There is no solution"
##    else:
##        print "Number of pigs: ", pigs
##        print "Number of chickens: ", chickens
##        print "Number of spiders: ", spiders

##Following programs are used to illustrate recursion
def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1: -1])

def fib(x):
    """Returns fibonacci of x, where x is a non- negative integer"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x - 2)


