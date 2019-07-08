def add(a, b):
	result = a + b
	print "Adding %d + %d = %d" % (a, b, result)
	return result

def subtract(a, b):
	result = a - b
	print "Subtracting %d - %d = %d" % (a, b, result)
	return result

def multiply(a, b):
	result = a * b
	print "Multiplying %d * %d = %d" % (a, b, result)
	return result

def divide(a, b):
	result = a / b
	print "Dividing %d / %d = %d" % (a, b, result)
	return result

print "Let's do some math with just functions!."

age = add( 45, 12)
height = subtract(120, 75)
weight = multiply(10, 6)
iq = divide(600, 3)

print "Age: %d, Height: %d, Weight: %d, IQ: %.2f" % (age, height, weight, iq)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes:", what, "can you do it by hand?"