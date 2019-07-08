import math

def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        val = input(requestMsg)
        if type(val) == type(1.0):
            inputOK = True
        else:
            print(errorMsg)
    return val

base = getFloat('Enter the base: ', 'Error: base must be a float')
height = getFloat('Enter the height: ', 'Error: height must be a float')

hyp = math.sqrt(base * base + height * height)

print 'Base: ' + str(base) + ',Height: ' + str(height) + ', Hypotenuse: ' + str(hyp)
