#the while.py script done as a function
def while_loop(nums, incr):
	i = 0
	numbers = []

	while i < nums:
		print "At the top i is %d" % i
		numbers.append(i)

		i += incr
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

no = while_loop(100, 4)
