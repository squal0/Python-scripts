#similar to the scripts with argv
def print_two(*args): #def tells python to make a function 'define'
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this one takes just one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothing'."

print_two("Superbi", "Squalo")
print_two_again("Oracion", "Seis")
print_one("Deadman: ")
print_none()